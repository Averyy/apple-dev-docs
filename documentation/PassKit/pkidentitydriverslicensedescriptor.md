# PKIdentityDriversLicenseDescriptor

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

An object for requesting information from a user’s driver’s license or equivalent document.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
class PKIdentityDriversLicenseDescriptor
```

## Mentions

- [Requesting identity data from a Wallet pass](requesting-identity-data-from-a-wallet-pass.md)

#### Overview

For the elements you request, the response contains the corresponding elements present in the user’s identity document. The table below maps the elements you request using [`PKIdentityElement`](pkidentityelement.md) with the ISO and American Association of Motor Vehicle Administrators (AAMVA) namespaces in the response.

> ❗ **Important**:  When you verify a person’s driving privileges from a U.S. driver’s license, use `domestic_driving_privileges` from the `org.iso.18013.5.1.aamva` namespace instead of `driving_privileges` from the `org.iso.18013.5.1` namespace because the former maps more directly to state laws. For more information about implementation, see [`AAMVA Mobile Driver’s License (mDL) Implementation Guidelines`](https://developer.apple.comhttps://www.aamva.org/topics/mobile-driver-license#?wst=4a3b89462cc2cff2cbe0c7accde57421).

The framework allows for requesting the Boolean [`age(atLeast:)`](pkidentityelement/age(atleast:).md) element for any age between `1` and `125` only if the issuer includes it. If an app requests [`age(atLeast:)`](pkidentityelement/age(atleast:).md) and the `age_over_XX` element isn’t present in the mobile driver’s license, the framework falls back to a request for the [`age`](pkidentityelement/age.md) element.

An app can’t include both an [`age(atLeast:)`](pkidentityelement/age(atleast:).md) element and an [`age`](pkidentityelement/age.md) element in the same request.

| Identity element | ISO namespace | AAMVA namespace |
| --- | --- | --- |
| `givenName` | `given_name` | `given_name_truncation`, `aka_given_name`, `name_suffix`, `aka_suffix` |
| `familyName` | `family_name` | `family_name_truncation`, `aka_family_name` |
| `portrait` | `portrait` |  |
| `address` | `resident_address`, `resident_city`, `resident_country`, `resident_postal_code` |  |
| `issuingAuthority` | `issuing_authority`, `issuing_jurisdiction`, `issuing_country`, `un_distinguishing_sign` |  |
| `documentExpirationDate` | `expiry_date` |  |
| `documentIssueDate` | `document_issue_date` |  |
| `documentNumber` | `document_number` |  |
| `drivingPrivileges` | `driving_privileges` | `domestic_driving_privileges` |
| `age` | `age_in_years` |  |
| `dateOfBirth` | `birth_date` |  |
| `age(atLeast: XX)` | `age_over_XX` |  |

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
- [class PKIdentityPhotoIDDescriptor](pkidentityphotoiddescriptor.md)
  An object you use to request information from a user’s photo ID or equivalent document.
- [class PKIdentityAnyOfDescriptor](pkidentityanyofdescriptor.md)
  An object you use to request information from multiple identity documents.
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

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkidentitydriverslicensedescriptor)*