# disconnect(from:)

**Framework**: Core Media I/O  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Disconnects a client from a source’s provider.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
func disconnect(from client: CMIOExtensionClient)
```

```objc
- (void) disconnectClient:(CMIOExtensionClient *) client;
```

## Parameters

- `client`: A client to disconnect to the source’s provider.

## See Also

### Managing Connections
- [func connect(to: CMIOExtensionClient) throws](./connect%28to%29.md)
  Connects a client to a source’s provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionprovidersource/disconnect(from:))*