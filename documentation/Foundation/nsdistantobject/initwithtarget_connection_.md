# initWithTarget:connection:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Initializes a newly allocated NSDistantObject as a remote proxy for `target`, which is an id in another thread or another application’s address space.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```objc
- (instancetype) initWithTarget:(id) target connection:(NSConnection *) connection;
```

#### Return Value

An `NSDistantObject` object initialized as a remote proxy for `target`. If a proxy for `target` and `connection` already exists, the receiver is released and the existing proxy is retained and returned.

#### Discussion

A remote proxy can’t be used until its connection’s peer has a local proxy representing `target` in the other application.

This is the designated initializer for remote proxies. It returns an initialized object, which might be different than the original receiver.

## Parameters

- `target`: An object in another thread or another application’s address space.
- `connection`: The connection to set as the `NSConnection` object for the returned proxy—it should have been created using the [`connectionWithRegisteredName:host:`](../nsconnection/connectionwithregisteredname_host_.md) class method.

## See Also

### Creating a Remote Proxy
- [+ proxyWithTarget:connection:](./proxywithtarget_connection_.md)
  Returns a remote proxy for a given object and connection, creating the proxy if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdistantobject/initwithtarget:connection:)*