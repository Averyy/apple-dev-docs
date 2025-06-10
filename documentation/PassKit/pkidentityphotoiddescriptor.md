# PKIdentityPhotoIDDescriptor

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

An object you use to request information from a user’s photo ID or equivalent document.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class PKIdentityPhotoIDDescriptor
```

## Mentions

- [Requesting identity data from a Wallet pass](requesting-identity-data-from-a-wallet-pass.md)

##### Discussion

Use this class to help create a credential in Wallet for chip-based identification, like a passport or US photo ID. This ID is available to use in person, within apps, and on the web.

For the elements you request, the response contains the corresponding elements present in the user’s identity document. The following table shows the mapping from [`PKIdentityElement`](pkidentityelement.md) to elements in the `PKIdentityPhotoIDDescriptor`. If the [`PKIdentityElement`](pkidentityelement.md) corresponds to more than one of the mobile doc elements, all of the elements are returned.

| Identity element | ISO 23220_1 namespace | Description |
| --- | --- | --- |
| `familyNameElement` | `family_name_unicode`, `family_name_latin1` | Last name, surname, or primary identifier, of the holder. |
| `givenNameElement` | `given_name_unicode`, `given_name_latin1` | First name(s), other name(s), or secondary identifier, of the holder. |
| `portraitElement` | `portrait` | Portrait data as specified in ISO/IEC 18013-2:2020, C.4.5. |
| `addressElement` | `resident_address_unicode`, `resident_city_unicode`, `resident_city_latin1`, `resident_postal_code`, `resident_country` | The place where the ID holder resides and may be contacted. |
| `issuingAuthority` | `issuing_authority_unicode`, `issuing_subdivision`, `issuing_country` | The issuer of the ID. |
| `documentIssueDateElement` | `issue_date` | The issue date for the underlying physical ID. |
| `documentExpirationDateElement` | `expiry_date` | Date when the ID expires (Note: This is intended to be the date of the underlying physical document, if appropriate. The mdoc-specific dates are included in the ValidityInfo within the MSO.) |
| `documentNumberElement` | `document_number` | The number assigned or calculated by the issuing authority. |
| `sexElement` | `sex_unicode` | The ID holder’s sex using values as defined in ISO/IEC 5218. |
| `dateOfBirthElement` | `birth_date_unicode` | The date when the ID holder was born. |
| `ageElement` | `age_in_years` | The age of the ID holder. |
| `ageThresholdElement` | `age_over_NN` | Age attestation used to convey to a verifier, in a data-minimized fashion, if the holder is older than a specified age. |

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [PKIdentityDocumentDescriptor](pkidentitydocumentdescriptor.md)

## See Also

- [Requesting identity data from a Wallet pass](requesting-identity-data-from-a-wallet-pass.md)
  Initiate a request for identity information by prompting a user for permission and decrypting a response payload.
- [class PKIdentityAnyOfDescriptor](pkidentityanyofdescriptor.md)
  An object you use to request information from multiple identity documents.
- [class PKIdentityDriversLicenseDescriptor](pkidentitydriverslicensedescriptor.md)
  An object for requesting information from a user’s driver’s license or equivalent document.
- [class PKAddIdentityDocumentMetadata](pkaddidentitydocumentmetadata.md)
  The object for specifying the metadata necessary to provision identity documents.
- [class PKAddIdentityDocumentConfiguration](pkaddidentitydocumentconfiguration.md)
  Configuration to define the identity document.
- [struct JPKIPassContents](jpkipasscontents.md)
  A set of actions for viewing and updating PINs, passwords, and signing abilities associated with digital identities on the JPKI applet.
- [class PKAddIdentityDocumentConfiguration](pkaddidentitydocumentconfiguration.md)
  Configuration to define the identity document.
- [class PKAddPassMetadataPreview](pkaddpassmetadatapreview.md)
  A preview object that contains information representing the pass you add to Wallet.
- [class PKIdentityDocumentMetadata](pkidentitydocumentmetadata.md)
  A set of configured metadata that defines the required information to add the corresponding pass to Wallet.
- [class PKIdentityNationalIDCardDescriptor](pkidentitynationalidcarddescriptor.md)
  An object for requesting information from a user’s national ID card.
- [class PKJapanIndividualNumberCardMetadata](pkjapanindividualnumbercardmetadata.md)
  A class that contains metadata indicating the specific product instance to provision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkidentityphotoiddescriptor)*