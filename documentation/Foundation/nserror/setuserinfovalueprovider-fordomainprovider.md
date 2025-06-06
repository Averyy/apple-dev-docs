# setUserInfoValueProvider(forDomain:provider:)

**Framework**: Foundation  
**Kind**: method

Specifies a block to call when the corresponding property is not present in the user info dictionary.

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
class func setUserInfoValueProvider(forDomain errorDomain: String, provider: ((any Error, String) -> Any?)? = nil)
```

#### Discussion

This method specifies a block that is called from the implementations of [`localizedDescription`](nserror/localizeddescription.md), [`localizedFailureReason`](nserror/localizedfailurereason.md), [`localizedRecoverySuggestion`](nserror/localizedrecoverysuggestion.md), [`localizedRecoveryOptions`](nserror/localizedrecoveryoptions.md), [`recoveryAttempter`](nserror/recoveryattempter.md), and [`helpAnchor`](nserror/helpanchor.md) when the underlying value for any of those properties is not present in the [`userInfo`](nserror/userinfo.md) dictionary of NSError instances with the specified domain.

A user info provider is optional, and allows localization and formatting of error messages to be done lazily, rather than populating the [`userInfo`](nserror/userinfo.md) at the time of creation. It is expected that only the “owner” of an [`NSError`](nserror.md) domain specifies the provider for the domain, and that this is done at most once. This method is not meant for consumers of errors to customize the [`userInfo`](nserror/userinfo.md) entries, and should not be used to customize the behaviors of error domains provided by the system.

The keys of a provider’s [`userInfo`](nserror/userinfo.md) dictionary correspond to the queried property, such as [`NSLocalizedDescriptionKey`](nslocalizeddescriptionkey.md) for the [`localizedDescription`](nserror/localizeddescription.md) property. The provider should return `nil` for any keys that it is unable to provide, as well as any keys it does not recognize (since the list of error keys may be extended in future releases). If an appropriate result for the requested key cannot be provided, return `nil` rather than choosing to manufacture a generic fallback response.

The provider block is executed synchronously at the time when a corresponding property is accessed. The results are not cached.

## Parameters

- `errorDomain`: The error domain of the provider.
- `provider`: A block to be executed synchronously at the time a corresponding property is accessed.

## See Also

- [class func userInfoValueProvider(forDomain: String) -> ((any Error, String) -> Any?)?](nserror/userinfovalueprovider(fordomain:).md)
  Returns any user info provider specified for a given error domain.
- [struct ErrorUserInfoKey](erroruserinfokey.md)
- [typealias UserInfoKey](nserror/userinfokey.md)
  These keys may exist in the user info dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nserror/setuserinfovalueprovider(fordomain:provider:))*