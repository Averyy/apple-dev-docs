# touchSurface

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

The element that represents the state of the user’s touch on the surface of the touchpad.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var touchSurface: GCControllerDirectionPad { get }
```

```objc
@property (nonatomic, readonly) GCControllerDirectionPad * touchSurface;
```

## Discussion

This element provides the recent or last touch positions on the two axes. Use the [`touchState`](./touchstate-swift.property.md) property to determine whether the user is currently touching the surface.

## See Also

### Getting the subelements
- [var button: GCControllerButtonInput](./button.md)
  The element that represents the button component on the touchpad.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollertouchpad/touchsurface)*