# focusEffect

**Framework**: UIKit  
**Kind**: property

The visual effect to apply when the item becomes focused.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor optional var focusEffect: UIFocusEffect? { get }
```

#### Discussion

A `nil` value indicates that the system shouldn’t apply any visual effects when the item becomes focused.

If you don’t implement this property, its value is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusitem/focuseffect)*