# TokensResponse

**Framework**: Device Management  
**Kind**: dictionary

The response object that contains the device token.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object TokensResponse
```

## Topics

### Supporting Objects
- [object SynchronizationTokens](synchronizationtokens.md)
  The server’s synchronization token.

## Properties

- `SyncTokens` (SynchronizationTokens) *(required)*: A dictionary of synchronization tokens that describes the state of different types of data on the server. The client uses these tokens to determine which endpoints it needs to use to fetch new or updated data on the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/tokensresponse)*