# serviceName

**Framework**: File Provider  
**Kind**: property  
**Required**: Yes

A name that uniquely identifies the service (reverse domain name notation is recommended).

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var serviceName: NSFileProviderServiceName { get }
```

## See Also

- [func makeListenerEndpoint() throws -> NSXPCListenerEndpoint](nsfileproviderservicesource/makelistenerendpoint.md)
  Returns an endpoint object that lets the host app communicate with the File Provider extension.
- [var isRestricted: Bool](nsfileproviderservicesource/isrestricted.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderservicesource/servicename)*