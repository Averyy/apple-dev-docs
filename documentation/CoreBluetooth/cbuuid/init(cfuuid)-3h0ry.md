# init(cfuuid:)

**Framework**: Core Bluetooth  
**Kind**: init  
**Role**: Initializer

Creates a Core Bluetooth UUID object from a Core Foundation UUID object.

**Availability**:
- iOS 5.0+ - Deprecated in 9.0
- iPadOS 5.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.7+ - Deprecated in 10.13
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

## Declaration

```swift
init(cfuuid theUUID: CFUUID)
```

```objc
+ (CBUUID *) UUIDWithCFUUID:(CFUUIDRef) theUUID;
```

#### Return Value

A new [`CBUUID`](../cbuuid.md) object for the specified UUID.

## Parameters

- `theUUID`: A UUID represented by a [`CFUUID`](../../CoreFoundation/cfuuid.md) object.

## See Also

### Creating New CBUUID Objects
- [init(string: String)](./init%28string%29.md)
  Creates a Core Bluetooth UUID object from a 16-, 32-, or 128-bit UUID string.
- [init(data: Data)](./init%28data%29.md)
  Creates a Core Bluetooth UUID object from a 16-, 32-, or 128-bit UUID data container.
- [init(nsuuid: UUID)](./init%28nsuuid%29-2amob.md)
  Creates a Core Bluetooth UUID object from a Foundation UUID object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbuuid/init(cfuuid:)-3h0ry)*