# addContact(_:)

**Framework**: Core MIDI  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) addContact:(MIDINetworkHost *) contact;
```

#### Return Value

[`true`](../../Swift/true.md) if the session successfully added the host, otherwise [`false`](../../Swift/false.md).

## Parameters

- `contact`: The MIDI network host to add.

## See Also

### Managing Contacts
- [func contacts() -> Set<MIDINetworkHost>](./contacts%28%29.md)
  Returns the array of network hosts.
- [func removeContact(MIDINetworkHost) -> Bool](./removecontact%28_%29.md)
  Removes a host as a contact.
- [let MIDINetworkNotificationContactsDidChange: String](../midinetworknotificationcontactsdidchange.md)
  Indicates that the list of contacts changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midinetworksession/addcontact(_:))*