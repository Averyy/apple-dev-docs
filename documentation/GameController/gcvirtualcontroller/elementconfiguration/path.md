# path

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

The Bezier path for the shape of an element.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var path: UIBezierPath? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIBezierPath * path;
```

## Discussion

Use this property to customize the image of an element. The framework only supports custom paths for button elements.

## See Also

### Configuring elements
- [var isHidden: Bool](./ishidden.md)
  A Boolean value that determines whether the virtual controller hides the element.
- [var actsAsTouchpad: Bool](./actsastouchpad.md)
  A Boolean value that determines whether the thumbstick element behaves as a touchpad.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcvirtualcontroller/elementconfiguration/path)*