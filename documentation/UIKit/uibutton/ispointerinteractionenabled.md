# isPointerInteractionEnabled

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that enables pointer interaction.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS 1.0+

## Declaration

```swift
var isPointerInteractionEnabled: Bool { get set }
```

```objc
@property (nonatomic, assign, readwrite, getter=isPointerInteractionEnabled) BOOL pointerInteractionEnabled;
```

#### Discussion

The default value of this property is [`false`](../../Swift/false.md).

## See Also

### Supporting pointer interactions
- [var isHovered: Bool](./ishovered.md)
  A Boolean value that indicates whether a pointer effect is active.
- [var pointerStyleProvider: UIButton.PointerStyleProvider?](./pointerstyleprovider-y4eb.md)
  A closure that returns the pointer style to use when the pointer hovers over the button.
- [typealias PointerStyleProvider](./pointerstyleprovider-swift.typealias.md)
  A type alias defining a closure that returns a pointer style to apply to a button.
- [typealias UIButtonPointerStyleProvider](../uibuttonpointerstyleprovider.md)
  A type alias defining a block that returns a pointer style to apply to a button.
- [pointerStyleProvider](./pointerstyleprovider-1d4d2.md)
  A block that returns the pointer style to use when the pointer hovers over the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/ispointerinteractionenabled)*