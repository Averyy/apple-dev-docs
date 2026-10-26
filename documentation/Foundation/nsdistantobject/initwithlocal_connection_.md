# initWithLocal:connection:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Initializes an `NSDistantObject` object as a local proxy for a given object.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```objc
- (instancetype) initWithLocal:(id) target connection:(NSConnection *) connection;
```

#### Return Value

An initialized `NSDistantObject` object that serves as a local proxy for `target`. If a proxy for `target` and `connection` already exists, the receiver is released and the existing proxy is retained and returned.

#### Discussion

Other applications connect to the proxy using the `NSConnection` [`connectionWithRegisteredName:host:`](../nsconnection/connectionwithregisteredname_host_.md) class method.

Local proxies should be considered private to their `NSConnection` objects. Only an `NSConnection` object should use this method to create them, and your code shouldn’t retain or otherwise use local proxies.

This is the designated initializer for local proxies. It returns an initialized object, which might be different than the original receiver

## Parameters

- `target`: An object in the receiver’s address space.
- `connection`: The connection for the returned proxy.

## See Also

### Creating a Local Proxy
- [+ proxyWithLocal:connection:](./proxywithlocal_connection_.md)
  Returns a local proxy for a given object and connection, creating the proxy if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdistantobject/initwithlocal:connection:)*