# NIConfiguration

**Framework**: Nearby Interaction  
**Kind**: class  
**Role**: Class

An abstract base class for interaction configurations.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- watchOS 7.3+

## Declaration

```swift
class NIConfiguration
```

```objc
@interface NIConfiguration : NSObject
```

## Mentions

- [Initiating and maintaining a session](./initiating-and-maintaining-a-session.md)

## Overview

The [`NIConfiguration`](./niconfiguration.md) class serves as the common identity for configuration objects. Don’t instantiate this class directly. Instead, instantiate one if its concrete subclasses: [`NINearbyPeerConfiguration`](./ninearbypeerconfiguration.md) or [`NINearbyAccessoryConfiguration`](./ninearbyaccessoryconfiguration.md). Use your configuration object to specify the features you want to enable in a Nearby Interaction session, and pass the object to the session’s [`run(_:)`](./nisession/run%28_%29.md) method.

## Topics

### Initializers
- [init?(coder: NSCoder)](./niconfiguration/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [NIDLTDOAConfiguration](./nidltdoaconfiguration.md)
- [NINearbyAccessoryConfiguration](./ninearbyaccessoryconfiguration.md)
- [NINearbyPeerConfiguration](./ninearbypeerconfiguration.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/niconfiguration)*