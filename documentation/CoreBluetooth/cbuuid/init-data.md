# init(data:)

**Framework**: Core Bluetooth  
**Kind**: init

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

#### Return Value

A new [`CBUUID`](cbuuid.md) object for the specified UUID data.

#### Discussion

This method is useful when handling the UUID of a Bluetooth attribute in raw bytes.

## Parameters

- `theData`: Data containing a 16-, 32-, or 128-bit UUID.

## See Also

- [init(string: String)](cbuuid/init(string:).md)
  Creates a Core Bluetooth UUID object from a 16-, 32-, or 128-bit UUID string.
- [init(cfuuid: CFUUID)](cbuuid/init(cfuuid:).md)
  Creates a Core Bluetooth UUID object from a Core Foundation UUID object.
- [init(nsuuid: UUID)](cbuuid/init(nsuuid:).md)
  Creates a Core Bluetooth UUID object from a Foundation UUID object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbuuid/init(data:))*