# MIDINetworkSession

**Framework**: Core MIDI  
**Kind**: class

An object that represents a pairing of a source and destination.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class MIDINetworkSession
```

#### Overview

A session can have any number of connections. The system broadcasts output to all connections, and merges input from multiple connections.

## Topics

### Configuring a Session
- [class func `default`() -> MIDINetworkSession](midinetworksession/default.md)
  Returns the default singleton session.
- [var isEnabled: Bool](midinetworksession/isenabled.md)
  A Boolean value that determines whether the session is enabled.
- [var connectionPolicy: MIDINetworkConnectionPolicy](midinetworksession/connectionpolicy.md)
  The policy that determines who can connect to this session.
### Inspecting a Sessions
- [var localName: String](midinetworksession/localname.md)
  The name of this session’s entity.
- [var networkName: String](midinetworksession/networkname.md)
  The name with which this session advertises itself over Bonjour.
- [var networkPort: Int](midinetworksession/networkport.md)
  The session’s UDP port.
- [func sourceEndpoint() -> MIDIEndpointRef](midinetworksession/sourceendpoint.md)
  Returns the session’s source endpoint.
- [func destinationEndpoint() -> MIDIEndpointRef](midinetworksession/destinationendpoint.md)
  Returns the session’s destination endpoint.
### Managing Connections
- [func connections() -> Set<MIDINetworkConnection>](midinetworksession/connections.md)
  Returns the session’s set of MIDI network connections.
- [func addConnection(MIDINetworkConnection) -> Bool](midinetworksession/addconnection(_:).md)
  Adds a new connection to this session.
- [func removeConnection(MIDINetworkConnection) -> Bool](midinetworksession/removeconnection(_:).md)
  Removes a connection from this session.
### Managing Contacts
- [func contacts() -> Set<MIDINetworkHost>](midinetworksession/contacts.md)
  Returns the array of network hosts.
- [func addContact(MIDINetworkHost) -> Bool](midinetworksession/addcontact(_:).md)
  Adds a host as a contact.
- [func removeContact(MIDINetworkHost) -> Bool](midinetworksession/removecontact(_:).md)
  Removes a host as a contact.
- [let MIDINetworkNotificationContactsDidChange: String](midinetworknotificationcontactsdidchange.md)
  Indicates that the list of contacts changed.
### Observing State Changes
- [let MIDINetworkNotificationSessionDidChange: String](midinetworknotificationsessiondidchange.md)
  Indicates that other aspects of the session changed, such as the connection list, connection policy, and so on.

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

- [class MIDINetworkHost](midinetworkhost.md)
  An object that represents the host’s network address.
- [class MIDINetworkConnection](midinetworkconnection.md)
  An object that connects a session to a host.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midinetworksession)*