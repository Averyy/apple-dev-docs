# init(nsuuid:)

**Framework**: Core Bluetooth  
**Kind**: init

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

#### Return Value

A new [`CBUUID`](cbuuid.md) object for the specified UUID.

## Parameters

- `theUUID`: A UUID represented by an   object.

## See Also

- [init(string: String)](cbuuid/init(string:).md)
  Creates a Core Bluetooth UUID object from a 16-, 32-, or 128-bit UUID string.
- [init(data: Data)](cbuuid/init(data:).md)
  Creates a Core Bluetooth UUID object from a 16-, 32-, or 128-bit UUID data container.
- [init(cfuuid: CFUUID)](cbuuid/init(cfuuid:).md)
  Creates a Core Bluetooth UUID object from a Core Foundation UUID object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbuuid/init(nsuuid:))*