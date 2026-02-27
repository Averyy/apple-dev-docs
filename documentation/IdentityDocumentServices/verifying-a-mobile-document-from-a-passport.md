# Verifying a mobile document from a passport

**Framework**: IdentityDocumentServices

Validate a response from mobile document information derived from a passport.

#### Overview

Beginning in iOS 26.1 and watchOS 26.1, people can add passports in the form of mobile documents (mdocs) to their Wallet using a valid government-issued passport. If approved, those credentials are signed by Apple and provisioned to an iOS or watchOS device. You can validate a passport Digital ID response using the ISO/IEC 23220-2 standard. It inherits the functionality of ISO 18013-5 standard.

A Digital ID is a way for people to securely create an ID in Wallet using information from their U.S. passport and present their ID with an iPhone or Apple Watch. You can verify the authenticity, integrity, and validity of a Digital ID response in following scenarios:

- Your iOS app accepts mdocs using the Verify with Wallet API. For more information, see [`Requesting identity data from a Wallet pass`](https://developer.apple.com/documentation/PassKit/requesting-identity-data-from-a-wallet-pass).
- Your website accepts Verify with Wallet on the Web. For more information, see [`Requesting a mobile document on the web`](requesting-a-mobile-document-on-the-web.md) and [`Implementing as an identity document provider`](implenting-as-an-identity-document-provider.md).
- Your iOS app reads the mdoc’s response using [`ProximityReader`](https://developer.apple.com/documentation/ProximityReader)’s  [`MobilePhotoIDRawDataRequest`](https://developer.apple.com/documentation/ProximityReader/MobilePhotoIDRawDataRequest).
- Your ISO 18013-5 capable terminal wants to accept mdoc responses.

> **Note**: Using the [`MobileDocumentDisplayRequest`](https://developer.apple.com/documentation/ProximityReader/MobileDocumentDisplayRequest) or [`MobilePhotoIDDataRequest`](https://developer.apple.com/documentation/ProximityReader/MobilePhotoIDDataRequest) API in the [`ProximityReader`](https://developer.apple.com/documentation/ProximityReader) framework automatically verifies Digital IDs.

#### Verify the Passport Mobile Document Response

You can validate a Digital ID response by verifying the issuer and device signatures.

The following object shows an mdoc’s response containing an array of documents and its structure, as defined in Section 8.3.2.1.2.3 of the ISO/IEC 18013-5:

```other
DeviceResponse 
 version
 [documents]  
     docType
     issuerSigned
         issuerNameSpaces (credential data)
         issuerAuth
             MSO (Mobile Security Object)
                version 
                validityInfo
                deviceKeyInfo
                status
                     identifier_list
     deviceSigned
         nameSpaces (device-signed data, if any)
         deviceAuth
     errors
```

> ❗ **Important**: If your system or fraud rules require assurance that the original government-issued document the credential is derived from is still valid, supplement Digital ID presentment with other validation methods. Digital ID isn’t connected to the government-issued document’s system of record or any associated lost and stolen document revocation lists.

The following steps can validate an mdoc’s response by verifying the issuer and device signatures:

- Decode the `deviceResponse`.
- Verify issuer signatures.
- Verify device signatures.

The following table is a list of elements in the ISO/IEC 23220 issuer namespace:

| ISO 23220 namespace | Value type | Description |
| --- | --- | --- |
| `family_name_unicode` | String | The Digital ID holder’s last name, surname, or primary identifier. |
| `given_name_unicode` | String | The Digital ID holder’s first name(s), other name(s), or secondary identifiers. |
| `family_name_latin1` | String | The Digital ID holder’s last name, surname, or primary identifier in Latin-1 characters. |
| `given_name_latin1` | String | The Digital ID holder’s first name(s), other name(s), or secondary identifiers in Latin-1 characters. |
| `birth_date` | Date | A nested `birth_date` object. Contains the Digital ID holder’s nested `birth_date` full date (day, month, and year). Also contains an optional approximate birth date in the string. |
| `portrait` | Byte String | Portrait data as specified in ISO/IEC 18013-2:2020, C.4.5. |
| `issue_date` | Date | The issuing date of the Digital ID. This is intended to be the date of the underlying physical document, if appropriate. The mdoc-specific dates are included in the `ValidityInfo` within the MSO. |
| `expiry_date` | Date | The Digital ID expiration date. This is intended to be the date of the underlying physical document, if appropriate. The mdoc-specific dates are included in the `ValidityInfo` within the MSO. |
| `issuing_authority_unicode` | String | The issuing authority name. |
| `issuing_country` | String | The Alpha-2 country code, as defined in ISO 3166-1, of the issuing authority’s country or territory. This value is the same as the IACA’s `countryName`. |
| `age_in_years` | Integer | The Digital ID holder’s age in years. |
| `age_over_NN` | Boolean | The age attestation used to convey to a verifier, in a data-minimized fashion, if the holder is as old or older than a specified age, or if the holder is younger than a specified age. |
| `age_birth_year` | Integer | The year when the Digital ID holder was born. |
| `portrait_capture_date` | Date | The date the portrait was taken. |
| `sex` | Integer | The Digital ID holder’s sex using values as defined in ISO/IEC 5218 (0 = Not Known, 1 = Male, 2 = Female, 9 = Nonapplicable). |
| `nationality` | String | The nationality of the holder as a two-letter country code (alpha-2 code) defined in ISO 3166-1a. |
| `document_number` | String | The number assigned or calculated by the issuing authority. |
| `issuing_authority_latin1` | String | The Digital ID-issuing authority name in Latin-1 characters. |

#### Decode the Device Response

The device response is a [`CBOR (RFC 8949 Concise Binary Object Representation)`](https://developer.apple.comhttps://cbor.io) encoded byte array. You can check the validity of the response by using a CBOR library or parser in your chosen programming language.

A valid Digital ID device response has:

- A version equal to or greater than 1.0
- A nonempty documents object
- A `docType` that matches the expected value of `org.iso.23220.photoid.1`

If this step fails, you can choose to allow users to retry or fall back to a different verification method.

#### Validate the Device Response and Mobile Security Object

You can validate the `deviceResponse` by verifying the issuer and device signatures. Section 9.1.2 of ISO/IEC 18013-5 defines a procedure for validating the issuer data in the device response. This procedure helps your app authenticate data to ensure it comes from a source you trust.

Before you extract the issuer-signed data, you need to first validate the Mobile Security Object (MSO), its validity period, and the revocation list, then verify the issuer authentication hashes.

The MSO serves as a cryptographic anchor for the passport mdoc. Apple, the issuing authority, digitally signs this object. After it’s signed, it can’t be modified without invalidating the signature. The MSO expiration is set to 35 days, passport expiration, or birth date, whichever occurs first.

You can see a complete list for validating the device response and MSO in Section 9.1.2 of ISO/IEC 18013-5. The following is a nonexhaustive, high-level list to validate the MSO:

- Check that the signature attached to the MSO is correct.
- Ensure the MSO version is at least 1.0 and not higher than the version of the device response.
- Ensure the date properties of `validityInfo` are valid.
- Ensure the `docType` matches the `deviceResponse`,  `org.iso.23220.photoid.1`.

Next, validate the document signer certificate, which signs the MSO. You can validate the document signer certificate by doing the following:

- Ensure that you’ve validated the [`Apple Issuing Authority root CA (IACA)`](https://developer.apple.comhttps://www.apple.com/certificateauthority/apki202505/) and added it to your trust store. The IACA root CA certificates and associated policy documents and agreements are available in ISO/IEC 18013-5 section 9.1.2.
- Ensure that there’s a valid X.509 chain of trust to the Apple Issuing Authority Certificate Authority (IACA).
- Verify that the issuer is the same as the subject of the Apple IACA certificate.
- Verify that the certificate chain matches the certificate profile requirements described in Table B.3 of ISO/IEC 18013-5.
- Verify that `countryName` exists and contains a ISO 3166-1 alpha-2 code as per ISO/IEC 18013-5.
- Verify that all certificates are active.

After you validate the MSO and its validity period and you verify the issuer authentication hashes, you can validate the MSO revocation list, which adds an extra layer of security. The MSO object contains a status structure with a publicly accessible URL that points to an MSO revocation list.

Because the MSO revocation list is signed daily, each partition consists of a `COSE_Sign1` structure that contains the leaf certificate used to validate the signature of the KRL partition. The leaf and intermediate CA certificate are in the `COSE_Sign1` header and are checked against the root certificate, as defined by ISO/IEC 18013-5 second amendment section 9.1.2.6.

> **Note**: Apple systems generate the revocation list when a Digital ID is removed from Wallet, becomes inactive for more than 60 days, or is deleted by the user in Find My or via Apple Care. The list doesn’t contain government-sourced data. For offline use cases, download and cache all partitions with a maximum cache duration of one day.

#### Validate the Data Elements

Verify that the user information in the response matches the data from the issuing authority. The MSO includes an array of digests or hashes, covering every element in the mdoc.

To validate the date elements, ensure that each data element in the response matches its digest in the MSO by doing the following:

- Get the `digestAlgorithm` from the MSO as defined on ISO/IEC 18013-5 section 9.1.2.5.
- Get the `valueDigests` from the MSO.
- Validate each namespace by computing the digest for each signed item.
- Make sure its digest is present in the issuer authentication.

There can be more digests than you see in the `issuerSigned` items structure because you only receive signed items for each element you request.

#### Verify the Device Signatures

Section 9.1.3 of ISO/IEC 18013-5 defines a procedure for authenticating mdocs. This procedure helps your app verify that the response came from the issued device. Using this procedure helps prevent mdoc cloning to an unauthorized device and intermediary attacks. Digital ID credentials use Elliptic Curve Digital Signature Algorithm (ECDSA) for mdoc authentication.

You can see a complete list for verifying the device signature in Section 9.1.2 of ISO/IEC 18013-5. The following is a nonexhaustive, high-level list for verifying the device signature:

- Get the `deviceKey` from `DeviceKeyInfo`, encoded as a `COSE_Key` from the MSO.
- Extract the `deviceSigned` structure.
- Confirm the `deviceKey` from the MSO matches the key used to sign the `deviceSigned` object by validating the `COSE_Sign1` signature in the `deviceSigned.deviceAuth` using the public key encoded in the MSO’s `COSE_Key`.

> **Note**: If verifying the device signatures fails, you can choose to reject the Digital ID presentment response and optionally prevent the use of fallback verification methods.

## See Also

- [Requesting a mobile document on the web](requesting-a-mobile-document-on-the-web.md)
  Send a request for mobile document information for apps installed on a device.
- [Implementing as an identity document provider](implenting-as-an-identity-document-provider.md)
  Add your app as an option for mobile document web presentment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/verifying-a-mobile-document-from-a-passport)*