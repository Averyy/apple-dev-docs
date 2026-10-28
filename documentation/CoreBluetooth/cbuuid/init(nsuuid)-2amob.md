# init(nsuuid:)

**Framework**: Core Bluetooth  
**Kind**: init  
**Role**: Initializer

Creates a Core Bluetooth UUID object from a Foundation UUID object.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(nsuuid theUUID: UUID)
```

```objc
+ (CBUUID *) UUIDWithNSUUID:(NSUUID *) theUUID;
```

## Return Value

A new [`CBUUID`](../cbuuid.md) object for the specified UUID.

## Parameters

- `theUUID`: A UUID represented by an [`NSUUID`](../../Foundation/nsuuid.md) object.

## See Also

### Creating New CBUUID Objects
- [init(string: String)](./init%28string%29.md)
  Creates a Core Bluetooth UUID object from a 16-, 32-, or 128-bit UUID string.
- [init(data: Data)](./init%28data%29.md)
  Creates a Core Bluetooth UUID object from a 16-, 32-, or 128-bit UUID data container.
- [init(cfuuid: CFUUID)](./init%28cfuuid%29-3h0ry.md)
  Creates a Core Bluetooth UUID object from a Core Foundation UUID object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbuuid/init(nsuuid:)-2amob)*