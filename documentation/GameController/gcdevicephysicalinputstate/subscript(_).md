# subscript(_:)

**Framework**: Game Controller  
**Kind**: subscript  
**Role**: Instance Subscript  
**Required**: Yes

Returns the element that the key specifies.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
subscript(key: String) -> (any GCPhysicalInputElement)? { get }
```

```objc
- (id<GCPhysicalInputElement>) objectForKeyedSubscript:(NSString *) key;
```

#### Return Value

The element that matches the key.

## Parameters

- `key`: A key that identifies an element.

## See Also

### Accessing elements
- [var elements: GCPhysicalInputElementCollection<any GCPhysicalInputElement>](./elements-46hgy.md)
  The device’s elements as key-value pairs for lookup by name.
- [var axes: GCPhysicalInputElementCollection<any GCAxisElement>](./axes-5u1xr.md)
  The device’s axes as key-value pairs for lookup by name.
- [var buttons: GCPhysicalInputElementCollection<any GCButtonElement>](./buttons-2ovae.md)
  The device’s buttons as key-value pairs for lookup by name.
- [var dpads: GCPhysicalInputElementCollection<any GCDirectionPadElement>](./dpads-7b4o3.md)
  The device’s directional pads as key-value pairs for lookup by name.
- [var switches: GCPhysicalInputElementCollection<any GCSwitchElement>](./switches-6dcny.md)
  The device’s switches as key-value pairs for lookup by name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdevicephysicalinputstate/subscript(_:))*