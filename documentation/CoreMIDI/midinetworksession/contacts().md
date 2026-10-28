# contacts()

**Framework**: Core MIDI  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSSet<MIDINetworkHost *> *) contacts;
```

## Return Value

The set of MIDI network host objects.

## See Also

### Managing Contacts
- [func addContact(MIDINetworkHost) -> Bool](./addcontact%28_%29.md)
  Adds a host as a contact.
- [func removeContact(MIDINetworkHost) -> Bool](./removecontact%28_%29.md)
  Removes a host as a contact.
- [let MIDINetworkNotificationContactsDidChange: String](../midinetworknotificationcontactsdidchange.md)
  Indicates that the list of contacts changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midinetworksession/contacts())*