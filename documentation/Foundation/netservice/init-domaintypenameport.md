# init(domain:type:name:port:)

**Framework**: Foundation  
**Kind**: init

Initializes the receiver for publishing a network service of type `type` at the socket location specified by `domain`, `name`, and `port`.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(domain: String, type: String, name: String, port: Int32)
```

#### Discussion

You use this method to create a service that you wish to publish on the network. Although you can also use this method to create a service you wish to resolve on the network, it is generally more appropriate to use the [`init(domain:type:name:)`](netservice/init(domain:type:name:).md) method instead.

When publishing a service, you must provide valid arguments in order to advertise your service correctly. If the host computer has access to multiple registration domains, you must create separate `NSNetService` objects for each domain. If you attempt to publish in a domain for which you do not have registration authority, your request may be denied.

It is acceptable to use an empty string for the `domain` argument when publishing or browsing a service, but do not rely on this for resolution.

This method is the designated initializer.

## Parameters

- `domain`: You can also use a   object to obtain a list of possible domains in which you can publish your service.
- `type`:  must contain both the service type and transport layer information. To ensure that the mDNS responder searches for services, as opposed to hosts, prefix both the service name and transport layer name with an underscore character (”_”). For example, to search for an HTTP service on TCP, you would use the type string “ ”. Note that the period character at the end of the string, which indicates that the domain name is an absolute name, is required.
- `name`: The name by which the service is identified to the network. The name must be unique. If you pass the empty string ( ), the system automatically advertises your service using the computer name as the service name.
- `port`: If your app is listening for connections on its own, the value of   must be a port number acquired by your application for the service.

## See Also

- [convenience init(domain: String, type: String, name: String)](netservice/init(domain:type:name:).md)
  Returns the receiver, initialized as a network service of a given type and sets the initial host information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservice/init(domain:type:name:port:))*