# PKIdentityNationalIDCardDescriptor

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

An object for requesting information from a user’s national ID card.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
class PKIdentityNationalIDCardDescriptor
```

## Mentions

- [Requesting identity data from a Wallet pass](requesting-identity-data-from-a-wallet-pass.md)

#### Discussion

For the elements you request, the response contains the corresponding elements present in the user’s identity document. The table below maps the elements you request using [`PKIdentityElement`](pkidentityelement.md) with the ISO and JP namespace in the response.

> **Note**:  You can retrieve elements specific to Japan only when you have set the API region to `JP`.

 You can retrieve elements specific to Japan only when you have set the API region to `JP`.

| Identity element | ISO namespace | JP namespace |
| --- | --- | --- |
| `givenName` |  | `full_name_unicode` |
| `familyName` |  | `full_name_unicode` |
| `portrait` |  | `portrait` |
| `address` |  | `resident_address_unicode, local_gov_code_unicode` |
| `documentNumber` |  | `individual_number_unicode` |
| `sex` | `sex` | `sex_unicode` |
| `age` | `age_in_years` |  |
| `dateOfBirth` | `birth_date` | `birth_date_unicode` |
| `age(atLeast: XX)` | `age_over_XX` |  |

This API requires a special entitlement issued by Apple. After you receive the entitlement, configure your Xcode project to use it:

1. Add the entitlement to the property list specified in your target.
2. In the `entitlements.plist` for the entitlement, add a new document-types item.
3. Add a new element string.

Building an app with this entitlement requires macOS 13 or later. For more information about the entitlement, see [`Getting started with the Verify with Wallet API`](https://developer.apple.comhttps://developer.apple.com/wallet/get-started-with-verify-with-wallet/).

## Topics

### Setting region information
- [var region: Locale.Region?](pkidentitynationalidcarddescriptor/region.md)
  A string used to specify the region associated with the ID.

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

- [struct JPKIPassContents](jpkipasscontents.md)
  A set of actions for viewing and updating PINs, passwords, and signing abilities associated with digital identities on the JPKI applet.
- [class PKAddIdentityDocumentConfiguration](pkaddidentitydocumentconfiguration.md)
  Configuration to define the identity document.
- [class PKAddPassMetadataPreview](pkaddpassmetadatapreview.md)
  A preview object that contains information representing the pass you add to Wallet.
- [class PKIdentityDocumentMetadata](pkidentitydocumentmetadata.md)
  A set of configured metadata defining the required information to add the corresponding pass to Wallet.
- [class PKJapanIndividualNumberCardMetadata](pkjapanindividualnumbercardmetadata.md)
  A class that contains metadata indicating the specific product instance to provision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkidentitynationalidcarddescriptor)*