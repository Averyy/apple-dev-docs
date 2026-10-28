# init(data:)

**Framework**: Core Bluetooth  
**Kind**: init  
**Role**: Initializer

Creates a Core Bluetooth UUID object from a 16-, 32-, or 128-bit UUID data container.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(data theData: Data)
```

```objc
+ (CBUUID *) UUIDWithData:(NSData *) theData;
```

## Return Value

A new [`CBUUID`](../cbuuid.md) object for the specified UUID data.

## Discussion

This method is useful when handling the UUID of a Bluetooth attribute in raw bytes.

## Parameters

- `theData`: Data containing a 16-, 32-, or 128-bit UUID.

## See Also

### Creating New CBUUID Objects
- [init(string: String)](./init%28string%29.md)
  Creates a Core Bluetooth UUID object from a 16-, 32-, or 128-bit UUID string.
- [init(cfuuid: CFUUID)](./init%28cfuuid%29-3h0ry.md)
  Creates a Core Bluetooth UUID object from a Core Foundation UUID object.
- [init(nsuuid: UUID)](./init%28nsuuid%29-2amob.md)
  Creates a Core Bluetooth UUID object from a Foundation UUID object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbuuid/init(data:))*