# authorizedToStartStream(for:)

**Framework**: Core Media I/O  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Determines whether to authorize an app to use this stream.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
func authorizedToStartStream(for client: CMIOExtensionClient) -> Bool
```

```objc
- (BOOL) authorizedToStartStreamForClient:(CMIOExtensionClient *) client;
```

#### Return Value

[`true`](../../Swift/true.md) if you authorize the app; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `client`: The client with authorization to check.

## See Also

### Managing a Stream
- [func startStream() throws](./startstream%28%29.md)
  Starts the stream of media data.
- [func stopStream() throws](./stopstream%28%29.md)
  Stops the stream of media data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstreamsource/authorizedtostartstream(for:))*