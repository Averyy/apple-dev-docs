# NSFileProviderServiceSource

**Framework**: File Provider  
**Kind**: protocol

A service that provides a custom communication channel between the host app and the File Provider extension.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
protocol NSFileProviderServiceSource
```

#### Overview

To implement a File Provider service, the [`NSFileProviderExtension`](nsfileproviderextension.md) subclass must override the [`supportedServiceSources(for:)`](nsfileproviderextension/supportedservicesources(for:).md) method and return the supported services.

For more information about creating services, see   [`NSFileProviderService`](https://developer.apple.com/documentation/Foundation/NSFileProviderService#2934440).

## Topics

### Accessing the Service
- [var serviceName: NSFileProviderServiceName](nsfileproviderservicesource/servicename.md)
  A name that uniquely identifies the service (reverse domain name notation is recommended).
- [func makeListenerEndpoint() throws -> NSXPCListenerEndpoint](nsfileproviderservicesource/makelistenerendpoint.md)
  Returns an endpoint object that lets the host app communicate with the File Provider extension.
- [var isRestricted: Bool](nsfileproviderservicesource/isrestricted.md)

## See Also

- [func supportedServiceSources(for: NSFileProviderItemIdentifier) throws -> [any NSFileProviderServiceSource]](nsfileproviderextension/supportedservicesources(for:).md)
  Return an array of service sources that let the host app perform actions associated with the specified item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderservicesource)*