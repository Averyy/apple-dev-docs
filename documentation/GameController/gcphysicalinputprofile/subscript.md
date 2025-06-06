# subscript(_:)

**Framework**: Game Controller  
**Kind**: subscript

Returns the element that the key specifies.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
subscript(key: String) -> GCControllerElement? { get }
```

#### Return Value

The element that matches the key.

#### Discussion

You can access elements of a profile using a subscript notation. For example, get the button with the X label from an instance of [`GCMicroGamepad`](gcmicrogamepad.md) using `microGamepad[”Button X”]`.

## Parameters

- `key`: A key that identifies an element.

## See Also

- [var elements: [String : GCControllerElement]](gcphysicalinputprofile/elements.md)
  The elements in the profile as key-value pairs for lookup by name.
- [var buttons: [String : GCControllerButtonInput]](gcphysicalinputprofile/buttons.md)
  The buttons in the profile as key-value pairs for lookup by name.
- [var axes: [String : GCControllerAxisInput]](gcphysicalinputprofile/axes.md)
  The axes in the profile as key-value pairs for lookup by name.
- [var dpads: [String : GCControllerDirectionPad]](gcphysicalinputprofile/dpads.md)
  The directional pads in the profile as key-value pairs for lookup by name.
- [var touchpads: [String : GCControllerTouchpad]](gcphysicalinputprofile/touchpads.md)
  The touchpads in the profile as key-value pairs for lookup by name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcphysicalinputprofile/subscript(_:))*