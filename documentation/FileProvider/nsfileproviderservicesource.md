# NSFileProviderServiceSource

**Framework**: File Provider  
**Kind**: protocol  
**Role**: Protocol

A service that provides a custom communication channel between the host app and the File Provider extension.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
protocol NSFileProviderServiceSource
```

```objc
@protocol NSFileProviderServiceSource
```

#### Overview

To implement a File Provider service, the [`NSFileProviderExtension`](./nsfileproviderextension.md) subclass must override the [`supportedServiceSources(for:)`](./nsfileproviderextension/supportedservicesources%28for%29.md) method and return the supported services.

For more information about creating services, see   [`NSFileProviderService`](../Foundation/nsfileproviderservice.md).

## Topics

### Accessing the Service
- [var serviceName: NSFileProviderServiceName](./nsfileproviderservicesource/servicename.md)
  A name that uniquely identifies the service (reverse domain name notation is recommended).
- [func makeListenerEndpoint() throws -> NSXPCListenerEndpoint](./nsfileproviderservicesource/makelistenerendpoint%28%29.md)
  Returns an endpoint object that lets the host app communicate with the File Provider extension.
- [var isRestricted: Bool](./nsfileproviderservicesource/isrestricted.md)

## See Also

### Working with services
- [func supportedServiceSources(for: NSFileProviderItemIdentifier) throws -> [any NSFileProviderServiceSource]](./nsfileproviderextension/supportedservicesources%28for%29.md)
  Return an array of service sources that let the host app perform actions associated with the specified item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderservicesource)*