# authorizedToStartStream(for:)

**Framework**: Core Media I/O  
**Kind**: method  
**Required**: Yes

Determines whether to authorize an app to use this stream.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
func authorizedToStartStream(for client: CMIOExtensionClient) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if you authorize the app; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `client`: The client with authorization to check.

## See Also

- [func startStream() throws](cmioextensionstreamsource/startstream.md)
  Starts the stream of media data.
- [func stopStream() throws](cmioextensionstreamsource/stopstream.md)
  Stops the stream of media data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstreamsource/authorizedtostartstream(for:))*