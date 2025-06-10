# ErrorUserInfoKey

**Framework**: Foundation  
**Kind**: struct

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct ErrorUserInfoKey
```

## Topics

### Type Properties
- [static let NSURLErrorKey: ErrorUserInfoKey](erroruserinfokey/nsurlerrorkey.md)
- [static let filePathErrorKey: ErrorUserInfoKey](erroruserinfokey/filepatherrorkey.md)
- [static let helpAnchorErrorKey: ErrorUserInfoKey](erroruserinfokey/helpanchorerrorkey.md)
- [static let localizedDescriptionKey: ErrorUserInfoKey](erroruserinfokey/localizeddescriptionkey.md)
- [static let localizedFailureReasonErrorKey: ErrorUserInfoKey](erroruserinfokey/localizedfailurereasonerrorkey.md)
- [static let localizedRecoveryOptionsErrorKey: ErrorUserInfoKey](erroruserinfokey/localizedrecoveryoptionserrorkey.md)
- [static let localizedRecoverySuggestionErrorKey: ErrorUserInfoKey](erroruserinfokey/localizedrecoverysuggestionerrorkey.md)
- [static let recoveryAttempterErrorKey: ErrorUserInfoKey](erroruserinfokey/recoveryattemptererrorkey.md)
- [static let stringEncodingErrorKey: ErrorUserInfoKey](erroruserinfokey/stringencodingerrorkey.md)
- [static let underlyingErrorKey: ErrorUserInfoKey](erroruserinfokey/underlyingerrorkey.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class func setUserInfoValueProvider(forDomain: String, provider: ((any Error, String) -> Any?)?)](nserror/setuserinfovalueprovider(fordomain:provider:).md)
  Specifies a block to call when the corresponding property is not present in the user info dictionary.
- [class func userInfoValueProvider(forDomain: String) -> ((any Error, String) -> Any?)?](nserror/userinfovalueprovider(fordomain:).md)
  Returns any user info provider specified for a given error domain.
- [typealias UserInfoKey](nserror/userinfokey.md)
  These keys may exist in the user info dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/erroruserinfokey)*