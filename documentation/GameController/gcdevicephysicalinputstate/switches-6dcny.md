# switches

**Framework**: Game Controller  
**Kind**: property

The device’s switches as key-value pairs for lookup by name.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+

## Declaration

```swift
var switches: GCPhysicalInputElementCollection<any GCSwitchElement> { get }
```

## See Also

- [var elements: GCPhysicalInputElementCollection<any GCPhysicalInputElement>](gcdevicephysicalinputstate/elements-46hgy.md)
  The device’s elements as key-value pairs for lookup by name.
- [var axes: GCPhysicalInputElementCollection<any GCAxisElement>](gcdevicephysicalinputstate/axes-5u1xr.md)
  The device’s axes as key-value pairs for lookup by name.
- [var buttons: GCPhysicalInputElementCollection<any GCButtonElement>](gcdevicephysicalinputstate/buttons-2ovae.md)
  The device’s buttons as key-value pairs for lookup by name.
- [var dpads: GCPhysicalInputElementCollection<any GCDirectionPadElement>](gcdevicephysicalinputstate/dpads-7b4o3.md)
  The device’s directional pads as key-value pairs for lookup by name.
- [subscript(String) -> (any GCPhysicalInputElement)?](gcdevicephysicalinputstate/subscript(_:).md)
  Returns the element that the key specifies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdevicephysicalinputstate/switches-6dcny)*