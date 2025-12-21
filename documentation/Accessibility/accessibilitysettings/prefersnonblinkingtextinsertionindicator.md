# prefersNonBlinkingTextInsertionIndicator

**Framework**: Accessibility  
**Kind**: property

A Boolean value that indicates whether the system setting to prefer a nonblinking cursor in editable text fields is on.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
static var prefersNonBlinkingTextInsertionIndicator: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) if the system setting for Prefer Non-Blinking Cursor is on; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false). This preference is relevant for apps that draw custom insertion indicators.

## See Also

- [static let prefersNonBlinkingTextInsertionIndicatorDidChangeNotification: NSNotification.Name](accessibilitysettings/prefersnonblinkingtextinsertionindicatordidchangenotification.md)
  A notification that posts when the system setting to prefer a nonblinking cursor in editable text fields changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/accessibilitysettings/prefersnonblinkingtextinsertionindicator)*