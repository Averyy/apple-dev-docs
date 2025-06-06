# recoveryAttempter

**Framework**: Foundation  
**Kind**: property

The object in the user info dictionary corresponding to the [`NSRecoveryAttempterErrorKey`](nsrecoveryattemptererrorkey.md) key.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var recoveryAttempter: Any? { get }
```

#### Discussion

The recovery attempter must be an instance of a class that conforms to the [`NSSecureCoding`](nssecurecoding.md) and NSErrorRecoveryAttempting protocols. It must also be able to correctly interpret an index in the [`localizedRecoveryOptions`](nserror/localizedrecoveryoptions.md) property.

If [`userInfo`](nserror/userinfo.md) doesn’t contain a value for [`NSRecoveryAttempterErrorKey`](nsrecoveryattemptererrorkey.md), this property is `nil`.

## See Also

- [var localizedRecoveryOptions: [String]?](nserror/localizedrecoveryoptions.md)
  An array containing the localized titles of buttons appropriate for displaying in an alert panel.
- [NSErrorRecoveryAttempting](nserrorrecoveryattempting.md)
  A set of methods that provide options to recover from an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nserror/recoveryattempter)*