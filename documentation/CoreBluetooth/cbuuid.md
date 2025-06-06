# CBUUID

**Framework**: Core Bluetooth  
**Kind**: class

A universally unique identifier, as defined by Bluetooth standards.

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
class CBUUID
```

#### Overview

Instances of the [`CBUUID`](cbuuid.md) class represent the 128-bit universally unique identifiers (UUIDs) of attributes used in Bluetooth low energy communication, such as a peripheral’s services, characteristics, and descriptors. This class provides a number of factory methods for dealing with long UUIDs when developing your app. For example, instead of passing around the string representation of a 128-bit Bluetooth low energy attribute in your code, you can create a [`CBUUID`](cbuuid.md) object that represents it, and pass that around instead.

The Bluetooth Special Interest Group (SIG) publishes a list of commonly-used UUIDs, many of which are 16- or 32-bits for convenience. The [`CBUUID`](cbuuid.md) class provides methods that automatically transform these predefined shorter UUIDs into their 128-bit equivalent UUIDs. When you create a [`CBUUID`](cbuuid.md) object from a predefined 16- or 32-bit UUID, Core Bluetooth pre-fills the rest of the 128-bit UUID with the Bluetooth base UUID, as defined in the Bluetooth 4.0 specification, Volume 3, Part F, Section 3.2.1.

In addition to providing methods for creating [`CBUUID`](cbuuid.md) objects, this class defines constants that represent the UUIDs of the Bluetooth-defined characteristic descriptors, as defined in the Bluetooth 4.0 specification, Volume 3, Part G, Section 3.3.3.

## Topics

### Creating New CBUUID Objects
- [init(string: String)](cbuuid/init(string:).md)
  Creates a Core Bluetooth UUID object from a 16-, 32-, or 128-bit UUID string.
- [init(data: Data)](cbuuid/init(data:).md)
  Creates a Core Bluetooth UUID object from a 16-, 32-, or 128-bit UUID data container.
- [init(cfuuid: CFUUID)](cbuuid/init(cfuuid:).md)
  Creates a Core Bluetooth UUID object from a Core Foundation UUID object.
- [init(nsuuid: UUID)](cbuuid/init(nsuuid:).md)
  Creates a Core Bluetooth UUID object from a Foundation UUID object.
### Inspecting CBUUID Properties
- [var data: Data](cbuuid/data.md)
  The data of the UUID.
- [var uuidString: String](cbuuid/uuidstring.md)
  The UUID represented as a string.
### UUID Constants
- [Characteristic Descriptors](characteristic-descriptors.md)
  Values that represent the UUIDs of the characteristic descriptors.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CBManager](cbmanager.md)
  The abstract base class that manages central and peripheral objects.
- [class CBATTRequest](cbattrequest.md)
  A request that uses the Attribute Protocol (ATT).
- [class CBPeer](cbpeer.md)
  An object that represents a remote device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbuuid)*