# pointerStyleProvider

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A block that returns the pointer style to use when the pointer hovers over the button.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, copy, readwrite, nullable) UIButtonPointerStyleProvider pointerStyleProvider;
```

#### Discussion

To change the appearance of the pointer when it hovers over the button, create a [`UIButtonPointerStyleProvider`](../uibuttonpointerstyleprovider.md) block that returns a [`UIPointerStyle`](../uipointerstyle.md) describing the pointer shape and content effect. Then assign the closure to [`pointerStyleProvider`](./pointerstyleprovider-1d4d2.md). For more information, see [Enhancing your iPad app with pointer interactions](../enhancing-your-ipad-app-with-pointer-interactions.md).

## See Also

### Supporting pointer interactions
- [var isPointerInteractionEnabled: Bool](./ispointerinteractionenabled.md)
  A Boolean that enables pointer interaction.
- [var isHovered: Bool](./ishovered.md)
  A Boolean value that indicates whether a pointer effect is active.
- [typealias UIButtonPointerStyleProvider](../uibuttonpointerstyleprovider.md)
  A type alias defining a block that returns a pointer style to apply to a button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/pointerstyleprovider-1d4d2)*