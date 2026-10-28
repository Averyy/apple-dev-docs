# proxyWithTarget:connection:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns a remote proxy for a given object and connection, creating the proxy if necessary.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```objc
+ (id) proxyWithTarget:(id) target connection:(NSConnection *) connection;
```

## Return Value

A remote proxy for `target` and `connection`, creating the proxy if necessary

## Discussion

A remote proxy cannot be used until its connection’s peer has a local proxy representing `target` in the other application.

## Parameters

- `target`: An object in another thread or another application’s address space.
- `connection`: The connection to set as the `NSConnection` object for the returned proxy—it should have been created using the `NSConnection` [`connectionWithRegisteredName:host:`](../nsconnection/connectionwithregisteredname_host_.md) class method.

## See Also

### Creating a Remote Proxy
- [- initWithTarget:connection:](./initwithtarget_connection_.md)
  Initializes a newly allocated NSDistantObject as a remote proxy for `target`, which is an id in another thread or another application’s address space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdistantobject/proxywithtarget:connection:)*