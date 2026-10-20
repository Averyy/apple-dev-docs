# makeListenerEndpoint()

**Framework**: File Provider  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns an endpoint object that lets the host app communicate with the File Provider extension.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func makeListenerEndpoint() throws -> NSXPCListenerEndpoint
```

```objc
- (NSXPCListenerEndpoint *) makeListenerEndpointAndReturnError:(NSError **) error;
```

## See Also

### Accessing the Service
- [var serviceName: NSFileProviderServiceName](./servicename.md)
  A name that uniquely identifies the service (reverse domain name notation is recommended).
- [var isRestricted: Bool](./isrestricted.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderservicesource/makelistenerendpoint())*