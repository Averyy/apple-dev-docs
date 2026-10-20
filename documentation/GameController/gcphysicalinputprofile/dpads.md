# dpads

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

The directional pads in the profile as key-value pairs for lookup by name.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var dpads: [String : GCControllerDirectionPad] { get }
```

```objc
@property (nonatomic, strong, readonly) NSDictionary<NSString *,GCControllerDirectionPad *> * dpads;
```

#### Discussion

Use the [`GCInputDualShockTouchpadOne`](../gcinputdualshocktouchpadone-55wgz.md) name to access an element on a DualShock controller.

```swift
touchpadOne = physicalInputProfile.dpads[GCInputDualShockTouchpadOne]
```

## See Also

### Accessing elements by name or key
- [var elements: [String : GCControllerElement]](./elements.md)
  The elements in the profile as key-value pairs for lookup by name.
- [var buttons: [String : GCControllerButtonInput]](./buttons.md)
  The buttons in the profile as key-value pairs for lookup by name.
- [var axes: [String : GCControllerAxisInput]](./axes.md)
  The axes in the profile as key-value pairs for lookup by name.
- [var touchpads: [String : GCControllerTouchpad]](./touchpads.md)
  The touchpads in the profile as key-value pairs for lookup by name.
- [subscript(String) -> GCControllerElement?](./subscript%28_%29.md)
  Returns the element that the key specifies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcphysicalinputprofile/dpads)*