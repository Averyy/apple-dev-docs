# send(venueDescriptor:)

**Framework**: Immersive Media Support  
**Kind**: method

Sends a venue descriptor to all connected receivers.

**Availability**:
- macOS 26.0+

## Declaration

```swift
func send(venueDescriptor: VenueDescriptor) async throws
```

#### Discussion

- venueDescriptor: The `venueDescriptor` to send to all clients.

> **Note**: This function throws if anything fails while sending the venue descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivemediaremotepreviewsender/send(venuedescriptor:))*