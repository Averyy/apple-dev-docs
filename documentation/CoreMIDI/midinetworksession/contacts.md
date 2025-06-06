# contacts()

**Framework**: Core MIDI  
**Kind**: method

Returns the array of network hosts.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func contacts() -> Set<MIDINetworkHost>
```

#### Return Value

The set of MIDI network host objects.

## See Also

- [func addContact(MIDINetworkHost) -> Bool](midinetworksession/addcontact(_:).md)
  Adds a host as a contact.
- [func removeContact(MIDINetworkHost) -> Bool](midinetworksession/removecontact(_:).md)
  Removes a host as a contact.
- [let MIDINetworkNotificationContactsDidChange: String](midinetworknotificationcontactsdidchange.md)
  Indicates that the list of contacts changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midinetworksession/contacts())*