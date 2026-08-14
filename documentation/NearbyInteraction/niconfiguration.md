# NIConfiguration

**Framework**: Nearby Interaction  
**Kind**: class

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

## Mentions

- [Initiating and maintaining a session](initiating-and-maintaining-a-session.md)

#### Overview

The [`NIConfiguration`](niconfiguration.md) class serves as the common identity for configuration objects. Don’t instantiate this class directly. Instead, instantiate one if its concrete subclasses: [`NINearbyPeerConfiguration`](ninearbypeerconfiguration.md) or [`NINearbyAccessoryConfiguration`](ninearbyaccessoryconfiguration.md). Use your configuration object to specify the features you want to enable in a Nearby Interaction session, and pass the object to the session’s [`run(_:)`](nisession/run(_:).md) method.

## Topics

### Initializers
- [init?(coder: NSCoder)](niconfiguration/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Inherited By
- [NIDLTDOAConfiguration](nidltdoaconfiguration.md)
- [NINearbyAccessoryConfiguration](ninearbyaccessoryconfiguration.md)
- [NINearbyPeerConfiguration](ninearbypeerconfiguration.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/niconfiguration)*