# elements

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

The elements in the profile as key-value pairs for lookup by name.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var elements: [String : GCControllerElement] { get }
```

```objc
@property (nonatomic, strong, readonly) NSDictionary<NSString *,GCControllerElement *> * elements;
```

## Discussion

Use this property to access elements by name. For example, use the name `“Button A”` to get the face button of an extended gamepad profile.

```swift
button = physicalInputProfile.elements[“Button A”]
```

For more button names, see [Extended gamepad input names](../extended-gamepad-input-names.md).

## See Also

### Accessing elements by name or key
- [var buttons: [String : GCControllerButtonInput]](./buttons.md)
  The buttons in the profile as key-value pairs for lookup by name.
- [var axes: [String : GCControllerAxisInput]](./axes.md)
  The axes in the profile as key-value pairs for lookup by name.
- [var dpads: [String : GCControllerDirectionPad]](./dpads.md)
  The directional pads in the profile as key-value pairs for lookup by name.
- [var touchpads: [String : GCControllerTouchpad]](./touchpads.md)
  The touchpads in the profile as key-value pairs for lookup by name.
- [subscript(String) -> GCControllerElement?](./subscript%28_%29.md)
  Returns the element that the key specifies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcphysicalinputprofile/elements)*