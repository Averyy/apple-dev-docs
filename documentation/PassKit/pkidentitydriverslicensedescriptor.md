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

 When you verify a person’s driving privileges from a U.S. driver’s license, use `domestic_driving_privileges` from the `org.iso.18013.5.1.aamva` namespace instead of `driving_privileges` from the `org.iso.18013.5.1` namespace because the former maps more directly to state laws. For more information about implementation, see [`AAMVA Mobile Driver’s License (mDL) Implementation Guidelines`](https://developer.apple.comhttps://www.aamva.org/topics/mobile-driver-license#?wst=4a3b89462cc2cff2cbe0c7accde57421).

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

- [class PKIdentityIntentToStore](pkidentityintenttostore.md)
  An object that represents your intention to store an identity element or values derived from an identity element.
- [protocol PKIdentityDocumentDescriptor](pkidentitydocumentdescriptor.md)
  A type that describes the structure and behavior of an identity document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkidentitydriverslicensedescriptor)*