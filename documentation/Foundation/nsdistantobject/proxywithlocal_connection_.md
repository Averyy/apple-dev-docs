# proxyWithLocal:connection:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns a local proxy for a given object and connection, creating the proxy if necessary.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```objc
+ (id) proxyWithLocal:(id) target connection:(NSConnection *) connection;
```

#### Return Value

A local proxy for `target` and `connection`, creating it if necessary.

#### Discussion

Other applications connect to the proxy using the `NSConnection` [`connectionWithRegisteredName:host:`](../nsconnection/connectionwithregisteredname_host_.md) class method.

Local proxies should be considered private to their `NSConnection` objects. Only an `NSConnection` object should use this method to create them, and your code shouldn’t retain or otherwise use local proxies.

## Parameters

- `target`: An object in the receiver’s address space.
- `connection`: The connection for the returned proxy.

## See Also

### Related Documentation
- [Distributed Objects Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/DistrObjects.html#//apple_ref/doc/uid/10000102i)
### Creating a Local Proxy
- [- initWithLocal:connection:](./initwithlocal_connection_.md)
  Initializes an `NSDistantObject` object as a local proxy for a given object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdistantobject/proxywithlocal:connection:)*