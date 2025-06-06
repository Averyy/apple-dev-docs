# localizedFallbackTitle

**Framework**: Local Authentication  
**Kind**: property

The localized title for the fallback button in the dialog presented to the user during authentication.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
var localizedFallbackTitle: String? { get set }
```

#### Discussion

The system presents a fallback button when biometric authentication fails—for example, because the system doesn’t recognize the presented finger, or after several failed attempts to recognize the user’s face. Tapping the button lets the user revert to authentication using the device passcode or password instead.

Use the [`localizedFallbackTitle`](lacontext/localizedfallbacktitle.md) property to set a title for the fallback button. When the property is `nil`—as it is by default—the user sees an appropriate default title, like “Use Passcode”. Otherwise, provide a localized string that’s short and clear.

To eliminate the fallback option, set the fallback title to an empty string. This hides the button from the interface.

## See Also

- [var localizedReason: String](lacontext/localizedreason.md)
  The localized explanation for authentication shown in the dialog presented to the user.
- [var localizedCancelTitle: String?](lacontext/localizedcanceltitle.md)
  The localized title for the cancel button in the dialog presented to the user during authentication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/lacontext/localizedfallbacktitle)*