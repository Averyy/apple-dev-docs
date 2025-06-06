# EAAccessoryDelegate

**Framework**: External Accessory  
**Kind**: protocol

A protocol that defines an optional method for receiving notifications when the associated accessory object is disconnected.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
protocol EAAccessoryDelegate : NSObjectProtocol
```

## Topics

### Responding to Disconnection Events
- [func accessoryDidDisconnect(EAAccessory)](eaaccessorydelegate/accessorydiddisconnect(_:).md)
  Tells the delegate that the specified accessory was disconnected from the device.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any EAAccessoryDelegate)?](eaaccessory/delegate.md)
  The object that acts as the delegate of the accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalaccessory/eaaccessorydelegate)*