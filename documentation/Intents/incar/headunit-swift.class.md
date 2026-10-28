# INCar.HeadUnit

**Framework**: Intents  
**Kind**: class  
**Role**: Class

An object that contains the Bluetooth and iAP2 identifiers of the vehicle’s physical head unit.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class HeadUnit
```

```objc
@interface INCarHeadUnit : NSObject
```

## Overview

When the system connects to a vehicle’s physical head unit through CarPlay, it uses the head unit’s Bluetooth identifier to find the corresponding vehicle in the user’s My Vehicles collection by matching on the `bluetoothIdentifier` property of this object.

You create instances of this class when handling [`INListCarsIntent`](../inlistcarsintent.md) requests. For more information on handling the intent, see [`INListCarsIntentHandling`](../inlistcarsintenthandling.md).

## Topics

### Creating a Head Unit
- [init(bluetoothIdentifier: String?, iAP2Identifier: String?)](./headunit-swift.class/init%28bluetoothidentifier,iap2identifier%29.md)
  Creates a head unit object with the specified Bluetooth and iAP2 identifiers.
### Getting the Head Unit’s Attributes
- [var bluetoothIdentifier: String?](./headunit-swift.class/bluetoothidentifier.md)
  The physical head unit’s Bluetooth identifier.
- [var iAP2Identifier: String?](./headunit-swift.class/iap2identifier.md)
  The head unit’s iAP2 identifier.
### Initializers
- [init?(coder: NSCoder)](./headunit-swift.class/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSCoding](../../Foundation/nscoding.md)
- [NSCopying](../../Foundation/nscopying.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../../Foundation/nssecurecoding.md)

## See Also

### Getting the Car’s Head Unit
- [var headUnit: INCar.HeadUnit?](./headunit-swift.property.md)
  The Bluetooth and iAP2 identifiers of the electric vehicle’s physical head unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incar/headunit-swift.class)*