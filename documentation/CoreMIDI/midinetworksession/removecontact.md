# removeContact(_:)

**Framework**: Core MIDI  
**Kind**: method

Removes a host as a contact.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func removeContact(_ contact: MIDINetworkHost) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the session successfully removed the host, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `contact`: The host to remove.

## See Also

- [func contacts() -> Set<MIDINetworkHost>](midinetworksession/contacts.md)
  Returns the array of network hosts.
- [func addContact(MIDINetworkHost) -> Bool](midinetworksession/addcontact(_:).md)
  Adds a host as a contact.
- [let MIDINetworkNotificationContactsDidChange: String](midinetworknotificationcontactsdidchange.md)
  Indicates that the list of contacts changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midinetworksession/removecontact(_:))*