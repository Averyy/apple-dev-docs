# Host

**Framework**: Foundation  
**Kind**: class

A representation of an individual host on the network.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class Host
```

#### Overview

The [`Host`](host.md) class provides methods to access the network name and address information for a host. Instances of the [`Host`](host.md) class represent individual  on a network. Use [`Host`](host.md) objects  to get the current host’s names and addresses and to look up other hosts by name or by address.

To create an [`Host`](host.md) object, use the [`current()`](host/current().md), [`init(address:)`](host/init(address:).md), or [`init(name:)`](host/init(name:).md) class methods (don’t use `alloc` and `init`). These methods use available network administration services to discover all names and addresses for the host requested. They don’t attempt to contact the host itself, however. This approach avoids untimely delays due to a host being unavailable, but it may result in incomplete information about the host.

An [`Host`](host.md) object contains all of the network addresses and names discovered for a given host by the network administration services. Each [`Host`](host.md) object may contain several addresses and have more than one name. If an [`Host`](host.md) object has more than one name, the additional names are variations on the same name, typically the basic host name plus the fully qualified domain name. For example, with a host name `"sales"` in the domain `"anycorp.com"`, an [`Host`](host.md) object can hold both the names `"sales"` and `"sales.anycorp.com"`.

[`Host`](host.md) methods are thread-safe.

## Topics

### Creating Hosts
- [class func current() -> Self](host/current.md)
  Returns an `NSHost` object representing the host the process is running on.
- [convenience init(address: String)](host/init(address:).md)
  Returns the `NSHost` with the Internet address `address`.
- [convenience init(name: String?)](host/init(name:).md)
  Returns a host with a specific name.
### Getting Host Information
- [var address: String?](host/address.md)
  Returns one of the network addresses of the receiver.
- [var addresses: [String]](host/addresses.md)
  Returns all the network addresses of the receiver.
- [var name: String?](host/name.md)
  Returns one of the hostnames of the receiver.
- [var localizedName: String?](host/localizedname.md)
  Returns the name used as by default when publishing `NSNetServices`.
- [var names: [String]](host/names.md)
  Returns all the hostnames of the receiver.
### Comparing Hosts
- [func isEqual(to: Host) -> Bool](host/isequal(to:).md)
  Indicates whether the receiver represents the same host as another `NSHost` object.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class Port](port.md)
  An abstract class that represents a communication channel.
- [class SocketPort](socketport.md)
  A port that represents a BSD socket.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/host)*