# send(venueDescriptor:)

**Framework**: Immersive Media Support  
**Kind**: method

Sends a VenueDescriptor to all connected receivers.

**Availability**:
- macOS 26.0+ (Beta)

## Declaration

```swift
func send(venueDescriptor: VenueDescriptor) async throws
```

#### Discussion

> **Note**: This function will throw if anything fails while sending the venue descriptor.

## Parameters

- `venueDescriptor`: The venueDescriptor to be sent to all clients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivemediaremotepreviewsender/send(venuedescriptor:))*