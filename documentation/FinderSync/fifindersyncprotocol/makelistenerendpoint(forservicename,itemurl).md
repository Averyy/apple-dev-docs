# makeListenerEndpoint(forServiceName:itemURL:)

**Framework**: Finder Sync  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 10.10+

## Declaration

```swift
optional func makeListenerEndpoint(forServiceName serviceName: NSFileProviderServiceName, itemURL: URL) throws -> NSXPCListenerEndpoint
```

```objc
- (NSXPCListenerEndpoint *) makeListenerEndpointForServiceName:(NSFileProviderServiceName) serviceName itemURL:(NSURL *) itemURL andReturnError:(NSError **) error;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/findersync/fifindersyncprotocol/makelistenerendpoint(forservicename:itemurl:))*