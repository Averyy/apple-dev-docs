# sendVenueDescriptor(at:)

**Framework**: Immersive Media Support  
**Kind**: method

Sends an AIME to all connected receivers.

**Availability**:
- macOS 26.0+

## Declaration

```swift
func sendVenueDescriptor(at url: URL) async throws
```

#### Discussion

> **Note**: This function throws if anything fails while sending the venue descriptor, for example, if the url is invalid.

## Parameters

- `url`: The url containing a valid venue descriptor file with extension  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivemediaremotepreviewsender/sendvenuedescriptor(at:))*