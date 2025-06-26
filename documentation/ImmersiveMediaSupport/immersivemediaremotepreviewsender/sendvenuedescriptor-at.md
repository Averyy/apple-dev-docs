# sendVenueDescriptor(at:)

**Framework**: Immersive Media Support  
**Kind**: method

Sends an AIME (VenueDescriptor file) to all connected receivers.

**Availability**:
- macOS 26.0+ (Beta)

## Declaration

```swift
func sendVenueDescriptor(at url: URL) async throws
```

#### Discussion

> **Note**: This function will throw if anything fails while sending the venue descriptor, for example, if the url is invalid.

## Parameters

- `url`: The url containing a valid venue descriptor file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivemediaremotepreviewsender/sendvenuedescriptor(at:))*