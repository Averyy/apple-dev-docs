# init(domain:type:name:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Returns the receiver, initialized as a network service of a given type and sets the initial host information.

**Availability**:
- iOS 2.0+ - Deprecated in 27.2
- iPadOS 2.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.2+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use nw_connection_t or nw_listener_t in Network framework instead

## Declaration

```swift
convenience init(domain: String, type: String, name: String)
```

```objc
- (instancetype) initWithDomain:(NSString *) domain type:(NSString *) type name:(NSString *) name;
```

## Return Value

The receiver, initialized as a network service named `name` of type `type` in the domain `domain`.

## Discussion

This method is the appropriate initializer to use to resolve a service—to publish a service, use [`init(domain:type:name:port:)`](./init%28domain,type,name,port%29.md).

If you know the values for `domain`, `type`, and `name` of the service you wish to connect to, you can create an `NSNetService` object using this initializer and call [`resolve(withTimeout:)`](./resolve%28withtimeout%29.md) on the result.

You cannot use this initializer to publish a service. This initializer passes an invalid port number to the designated initializer, which prevents the service from being registered. Calling [`publish()`](./publish%28%29.md) on an `NSNetService` object initialized with this method generates a call to your delegate’s [`netService(_:didNotPublish:)`](../netservicedelegate/netservice%28_,didnotpublish%29.md) method with an [`NetService.ErrorCode.badArgumentError`](./errorcode-swift.enum/badargumenterror.md) error.

## Parameters

- `domain`: The domain for the service. To resolve in the default domains, pass in an empty string (`@""`). To limit resolution to the local domain, use `@"local."`.

  If you are creating this object to resolve a service whose information your app stored previously, you should set this to the domain in which the service was originally discovered.

  You can also use a `NSNetServiceBrowser` object to obtain a list of possible domains in which you can discover and resolve services.
- `type`: The network service type.

  `type` must contain both the service type and transport layer information. To ensure that the mDNS responder searches for services, as opposed to hosts, prefix both the service name and transport layer name with an underscore character (”_”). For example, to search for an HTTP service on TCP, you would use the type string “`_http._tcp.`”. Note that the period character at the end of the string, which indicates that the domain name is an absolute name, is required.
- `name`: The name of the service to resolve.

## See Also

### Related Documentation
- [NSNetServices and CFNetServices Programming Guide](https://developer.apple.com/library/archive/documentation/Networking/Conceptual/NSNetServiceProgGuide/Introduction.html#//apple_ref/doc/uid/TP40002736)
- [Bonjour Overview](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NetServices/Introduction.html#//apple_ref/doc/uid/10000119i)
### Creating Network Services
- [init(domain: String, type: String, name: String, port: Int32)](./init%28domain,type,name,port%29.md)
  Initializes the receiver for publishing a network service of type `type` at the socket location specified by `domain`, `name`, and `port`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservice/init(domain:type:name:))*