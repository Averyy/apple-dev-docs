# addContact(_:)

**Framework**: Core MIDI  
**Kind**: method

Adds a host as a contact.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func addContact(_ contact: MIDINetworkHost) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the session successfully added the host, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `contact`: The MIDI network host to add.

## See Also

- [func contacts() -> Set<MIDINetworkHost>](midinetworksession/contacts.md)
  Returns the array of network hosts.
- [func removeContact(MIDINetworkHost) -> Bool](midinetworksession/removecontact(_:).md)
  Removes a host as a contact.
- [let MIDINetworkNotificationContactsDidChange: String](midinetworknotificationcontactsdidchange.md)
  Indicates that the list of contacts changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midinetworksession/addcontact(_:))*