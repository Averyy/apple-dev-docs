# startStream()

**Framework**: Core Media I/O  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Starts the stream of media data.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
func startStream() throws
```

```objc
- (BOOL) startStreamAndReturnError:(NSError **) outError;
```

## See Also

### Managing a Stream
- [func authorizedToStartStream(for: CMIOExtensionClient) -> Bool](./authorizedtostartstream%28for%29.md)
  Determines whether to authorize an app to use this stream.
- [func stopStream() throws](./stopstream%28%29.md)
  Stops the stream of media data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstreamsource/startstream())*