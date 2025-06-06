# HMNetworkConfigurationProfileDelegate

**Framework**: HomeKit  
**Kind**: protocol

An interface that your app adopts to receive notifications about changes in the state of network access.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
protocol HMNetworkConfigurationProfileDelegate : NSObjectProtocol
```

## Topics

### Observing network access changes
- [func profileDidUpdateNetworkAccessMode(HMNetworkConfigurationProfile)](hmnetworkconfigurationprofiledelegate/profiledidupdatenetworkaccessmode(_:).md)
  Tells the delegate that the network access mode has changed.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any HMNetworkConfigurationProfileDelegate)?](hmnetworkconfigurationprofile/delegate.md)
  A delegate that HomeKit tells about changes in the state of network access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmnetworkconfigurationprofiledelegate)*