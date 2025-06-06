# localizedReason

**Framework**: Local Authentication  
**Kind**: property

The localized explanation for authentication shown in the dialog presented to the user.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
var localizedReason: String { get set }
```

#### Discussion

This property is overwritten if an authentication reason is provided in [`evaluatePolicy(_:localizedReason:reply:)`](lacontext/evaluatepolicy(_:localizedreason:reply:).md).

The localized string you present to the user should provide a clear reason for why you are requesting they authenticate themselves, and what action you will be taking based on that authentication. This string should be provided in the user’s current language and should be short and clear. It should not contain the app name, because that appears elsewhere in the authentication dialog. In macOS this appears in the dialog title, and in iOS this appears in the dialog subtitle.

## See Also

- [var localizedFallbackTitle: String?](lacontext/localizedfallbacktitle.md)
  The localized title for the fallback button in the dialog presented to the user during authentication.
- [var localizedCancelTitle: String?](lacontext/localizedcanceltitle.md)
  The localized title for the cancel button in the dialog presented to the user during authentication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/lacontext/localizedreason)*