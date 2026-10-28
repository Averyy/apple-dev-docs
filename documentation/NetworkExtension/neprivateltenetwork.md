# NEPrivateLTENetwork

**Framework**: Network Extension  
**Kind**: class  
**Role**: Class

The parameters of a private LTE network.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
class NEPrivateLTENetwork
```

```objc
@interface NEPrivateLTENetwork : NSObject
```

## Overview

Populate your manager’s [`matchPrivateLTENetworks`](./neapppushmanager/matchprivateltenetworks.md) with an array of objects of this type. The system starts the provider when the device’s current private LTE provider matches the properties of any member of the array.

## Topics

### Accessing network properties
- [var mobileCountryCode: String](./neprivateltenetwork/mobilecountrycode.md)
  The Mobile Country Code (MCC) of the private LTE network.
- [var mobileNetworkCode: String](./neprivateltenetwork/mobilenetworkcode.md)
  The Mobile Network Code (MNC) of the private LTE network.
- [var trackingAreaCode: String?](./neprivateltenetwork/trackingareacode.md)
  The Tracking Area Code of the private LTE network.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Matching Wi-Fi networks
- [var matchSSIDs: [String]](./neapppushmanager/matchssids.md)
  An array of Wi-Fi SSID strings that the system matches for local push activation.
- [var matchPrivateLTENetworks: [NEPrivateLTENetwork]](./neapppushmanager/matchprivateltenetworks.md)
  An array of private LTE networks that the system matches for local push activation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neprivateltenetwork)*