# serviceName

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A name that uniquely identifies the service (reverse domain name notation is recommended).

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var serviceName: NSFileProviderServiceName { get }
```

```objc
@property (nonatomic, copy, readonly) NSFileProviderServiceName serviceName;
```

## See Also

### Accessing the Service
- [func makeListenerEndpoint() throws -> NSXPCListenerEndpoint](./makelistenerendpoint%28%29.md)
  Returns an endpoint object that lets the host app communicate with the File Provider extension.
- [var isRestricted: Bool](./isrestricted.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderservicesource/servicename)*