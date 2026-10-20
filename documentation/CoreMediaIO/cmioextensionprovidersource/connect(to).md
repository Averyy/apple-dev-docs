# connect(to:)

**Framework**: Core Media I/O  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Connects a client to a source’s provider.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
func connect(to client: CMIOExtensionClient) throws
```

```objc
- (BOOL) connectClient:(CMIOExtensionClient *) client error:(NSError **) outError;
```

## Parameters

- `client`: A client to connect to a source’s provider.

## See Also

### Managing Connections
- [func disconnect(from: CMIOExtensionClient)](./disconnect%28from%29.md)
  Disconnects a client from a source’s provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionprovidersource/connect(to:))*