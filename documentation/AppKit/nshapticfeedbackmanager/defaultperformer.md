# defaultPerformer

**Framework**: AppKit  
**Kind**: property

Requests a haptic feedback performer object that is based on the current input device, accessibility settings, and user preferences.

**Availability**:
- macOS 10.11+

## Declaration

```swift
class var defaultPerformer: any NSHapticFeedbackPerformer { get }
```

#### Discussion

This method returns a haptic feedback performer object of type `NSHapticFeedbackPerformer` that is based on the current input device, accessibility settings, and user preferences. Because the current input device may change at any time, you should request the default performer whenever you need to provide haptic feedback to the user.

## See Also

- [protocol NSHapticFeedbackPerformer](nshapticfeedbackperformer.md)
  A set of methods and constants that a haptic feedback performer implements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nshapticfeedbackmanager/defaultperformer)*