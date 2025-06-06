# userInfoValueProvider(forDomain:)

**Framework**: Foundation  
**Kind**: method

Returns any user info provider specified for a given error domain.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func userInfoValueProvider(forDomain errorDomain: String) -> ((any Error, String) -> Any?)?
```

#### Return Value

The user info provider of the error domain, or `nil` if none is specified.

## Parameters

- `errorDomain`: The error domain of the user info provider.

## See Also

- [class func setUserInfoValueProvider(forDomain: String, provider: ((any Error, String) -> Any?)?)](nserror/setuserinfovalueprovider(fordomain:provider:).md)
  Specifies a block to call when the corresponding property is not present in the user info dictionary.
- [struct ErrorUserInfoKey](erroruserinfokey.md)
- [typealias UserInfoKey](nserror/userinfokey.md)
  These keys may exist in the user info dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nserror/userinfovalueprovider(fordomain:))*