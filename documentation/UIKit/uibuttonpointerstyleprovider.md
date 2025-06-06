# UIButtonPointerStyleProvider

**Framework**: UIKit  
**Kind**: typealias

A type alias defining a block that returns a pointer style to apply to a button.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS 1.0+

## Declaration

```swift
typealias UIButtonPointerStyleProvider = (UIButton, __UIPointerEffect, __UIPointerShape) -> UIPointerStyle?
```

#### Return Value

The pointer style to apply to the button when the pointer hovers over it. Return `nil` when you don’t want to apply a pointer style to the button.

#### Discussion

To change the appearance of the pointer when it hovers over the button, create a pointer style provider block and assign it to the button’s [`pointerStyleProvider`](uibutton/pointerstyleprovider-1d4d2.md) property.

## Parameters

- `button`: The button requesting the pointer style.
- `proposedEffect`: The content effect that the system suggests.
- `proposedShape`: The shape of the pointer that the system suggests.

## See Also

- [var isPointerInteractionEnabled: Bool](uibutton/ispointerinteractionenabled.md)
  A Boolean that enables pointer interaction.
- [var isHovered: Bool](uibutton/ishovered.md)
  A Boolean value that indicates whether a pointer effect is active.
- [var pointerStyleProvider: UIButton.PointerStyleProvider?](uibutton/pointerstyleprovider-y4eb.md)
  A closure that returns the pointer style to use when the pointer hovers over the button.
- [typealias PointerStyleProvider](uibutton/pointerstyleprovider-swift.typealias.md)
  A type alias defining a closure that returns a pointer style to apply to a button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibuttonpointerstyleprovider)*