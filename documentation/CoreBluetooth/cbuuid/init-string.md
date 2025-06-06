# init(string:)

**Framework**: Core Bluetooth  
**Kind**: init

Creates a Core Bluetooth UUID object from a 16-, 32-, or 128-bit UUID string.

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
init(string theString: String)
```

#### Return Value

A new [`CBUUID`](cbuuid.md) object for the specified UUID string.

#### Discussion

Specify 128-bit UUIDs as a string of hexadecimal digits punctuated by hyphens, for example, 68753A44-4D6F-1226-9C60-0050E4C00067. Specify 16- or 32-bit UUIDs as a string of 4 or 8 hexadecimal digits, respectively. For an example of how to use this method, see [`Services and Characteristics Are Identified by UUIDs`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/CoreBluetooth_concepts/PerformingCommonPeripheralRoleTasks/PerformingCommonPeripheralRoleTasks.html#//apple_ref/doc/uid/TP40013257-CH4-SW8) and [`Create Your Own UUIDs for Custom Services and Characteristics`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/CoreBluetooth_concepts/PerformingCommonPeripheralRoleTasks/PerformingCommonPeripheralRoleTasks.html#//apple_ref/doc/uid/TP40013257-CH4-SW9).

For more information, see [`Core Bluetooth Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/CoreBluetooth_concepts/AboutCoreBluetooth/Introduction.html#//apple_ref/doc/uid/TP40013257).

## Parameters

- `theString`: A string containing a 16-, 32-, or 128-bit UUID.

## See Also

- [init(data: Data)](cbuuid/init(data:).md)
  Creates a Core Bluetooth UUID object from a 16-, 32-, or 128-bit UUID data container.
- [init(cfuuid: CFUUID)](cbuuid/init(cfuuid:).md)
  Creates a Core Bluetooth UUID object from a Core Foundation UUID object.
- [init(nsuuid: UUID)](cbuuid/init(nsuuid:).md)
  Creates a Core Bluetooth UUID object from a Foundation UUID object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbuuid/init(string:))*