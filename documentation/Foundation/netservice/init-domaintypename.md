# init(domain:type:name:)

**Framework**: Foundation  
**Kind**: init

Returns the receiver, initialized as a network service of a given type and sets the initial host information.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(domain: String, type: String, name: String)
```

#### Return Value

The receiver, initialized as a network service named `name` of type `type` in the domain `domain`.

#### Discussion

This method is the appropriate initializer to use to resolve a service—to publish a service, use [`init(domain:type:name:port:)`](netservice/init(domain:type:name:port:).md).

If you know the values for `domain`, `type`, and `name` of the service you wish to connect to, you can create an `NSNetService` object using this initializer and call [`resolve(withTimeout:)`](netservice/resolve(withtimeout:).md) on the result.

You cannot use this initializer to publish a service. This initializer passes an invalid port number to the designated initializer, which prevents the service from being registered. Calling [`publish()`](netservice/publish().md) on an `NSNetService` object initialized with this method generates a call to your delegate’s [`netService(_:didNotPublish:)`](netservicedelegate/netservice(_:didnotpublish:).md) method with an [`NetService.ErrorCode.badArgumentError`](netservice/errorcode-swift.enum/badargumenterror.md) error.

## Parameters

- `domain`: You can also use a   object to obtain a list of possible domains in which you can discover and resolve services.
- `type`:  must contain both the service type and transport layer information. To ensure that the mDNS responder searches for services, as opposed to hosts, prefix both the service name and transport layer name with an underscore character (”_”). For example, to search for an HTTP service on TCP, you would use the type string “ ”. Note that the period character at the end of the string, which indicates that the domain name is an absolute name, is required.
- `name`: The name of the service to resolve.

## See Also

- [NSNetServices and CFNetServices Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Networking/Conceptual/NSNetServiceProgGuide/Introduction.html#//apple_ref/doc/uid/TP40002736)
- [Bonjour Overview](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NetServices/Introduction.html#//apple_ref/doc/uid/10000119i)
- [init(domain: String, type: String, name: String, port: Int32)](netservice/init(domain:type:name:port:).md)
  Initializes the receiver for publishing a network service of type `type` at the socket location specified by `domain`, `name`, and `port`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservice/init(domain:type:name:))*