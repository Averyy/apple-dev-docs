# switches

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

The device’s switches as key-value pairs for lookup by name.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```objc
@property (readonly) GCPhysicalInputElementCollection<NSString<GCSwitchElementName> *,id<GCSwitchElement>> * switches;
```

## See Also

### Accessing elements
- [elements](./elements-1shp2.md)
  The device’s elements as key-value pairs for lookup by name.
- [axes](./axes-80rx.md)
  The device’s axes as key-value pairs for lookup by name.
- [buttons](./buttons-3257g.md)
  The device’s buttons as key-value pairs for lookup by name.
- [dpads](./dpads-5yr9x.md)
  The device’s directional pads as key-value pairs for lookup by name.
- [subscript(String) -> (any GCPhysicalInputElement)?](./subscript%28_%29.md)
  Returns the element that the key specifies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdevicephysicalinputstate/switches-6bws2)*