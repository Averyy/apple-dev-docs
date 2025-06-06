# canBecomeFocused

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

A Boolean value that indicates whether the item can become focused.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var canBecomeFocused: Bool { get }
```

## Mentions

- [About focus interactions for Apple TV](about-focus-interactions-for-apple-tv.md)

#### Discussion

When the value of this property is [`false`](https://developer.apple.com/documentation/swift/false), the item is not focusable, even if it is visible in the user interface. For example, a subclass of [`UIControl`](uicontrol.md) returns [`false`](https://developer.apple.com/documentation/swift/false) when it is not enabled.

Returning [`true`](https://developer.apple.com/documentation/swift/true) in this property means that the item is capable of being focused; it does not guarantee that the item is always focusable. Focusability is ultimately determined by the system. For example, if an item is visually obscured or offscreen, it may not be focusable. In addition, objects that conform to this protocol may have their own unique limitations. For example, a [`UIView`](uiview.md) object is not focusable when user interaction is disabled, or when the view’s alpha value is equal to `0`.

## See Also

- [var isFocused: Bool](uifocusitem/isfocused.md)
  A Boolean value that indicates whether the item is currently focused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusitem/canbecomefocused)*