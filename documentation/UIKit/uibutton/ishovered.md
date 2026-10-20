# isHovered

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether a pointer effect is active.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var isHovered: Bool { get }
```

```objc
@property (nonatomic, assign, readonly, getter=isHovered) BOOL hovered;
```

#### Discussion

If you enable pointer interaction by setting [`isPointerInteractionEnabled`](./ispointerinteractionenabled.md), this property indicates the button has an active pointer effect.

## See Also

### Related Documentation
- [Pointer interactions](../pointer-interactions.md)
  Support pointer interactions in your custom controls and views.
### Supporting pointer interactions
- [var isPointerInteractionEnabled: Bool](./ispointerinteractionenabled.md)
  A Boolean that enables pointer interaction.
- [var pointerStyleProvider: UIButton.PointerStyleProvider?](./pointerstyleprovider-y4eb.md)
  A closure that returns the pointer style to use when the pointer hovers over the button.
- [typealias PointerStyleProvider](./pointerstyleprovider-swift.typealias.md)
  A type alias defining a closure that returns a pointer style to apply to a button.
- [typealias UIButtonPointerStyleProvider](../uibuttonpointerstyleprovider.md)
  A type alias defining a block that returns a pointer style to apply to a button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/ishovered)*