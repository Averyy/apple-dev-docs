# isPointerInteractionEnabled

**Framework**: UIKit  
**Kind**: property

A Boolean that enables pointer interaction.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isPointerInteractionEnabled: Bool { get set }
```

#### Discussion

The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var isHovered: Bool](uibutton/ishovered.md)
  A Boolean value that indicates whether a pointer effect is active.
- [var pointerStyleProvider: UIButton.PointerStyleProvider?](uibutton/pointerstyleprovider-y4eb.md)
  A closure that returns the pointer style to use when the pointer hovers over the button.
- [typealias PointerStyleProvider](uibutton/pointerstyleprovider-swift.typealias.md)
  A type alias defining a closure that returns a pointer style to apply to a button.
- [typealias UIButtonPointerStyleProvider](uibuttonpointerstyleprovider.md)
  A type alias defining a block that returns a pointer style to apply to a button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/ispointerinteractionenabled)*