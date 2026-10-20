# removeContact(_:)

**Framework**: Core MIDI  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) removeContact:(MIDINetworkHost *) contact;
```

#### Return Value

[`true`](../../Swift/true.md) if the session successfully removed the host, otherwise [`false`](../../Swift/false.md).

## Parameters

- `contact`: The host to remove.

## See Also

### Managing Contacts
- [func contacts() -> Set<MIDINetworkHost>](./contacts%28%29.md)
  Returns the array of network hosts.
- [func addContact(MIDINetworkHost) -> Bool](./addcontact%28_%29.md)
  Adds a host as a contact.
- [let MIDINetworkNotificationContactsDidChange: String](../midinetworknotificationcontactsdidchange.md)
  Indicates that the list of contacts changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midinetworksession/removecontact(_:))*