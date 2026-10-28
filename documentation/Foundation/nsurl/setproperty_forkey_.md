# setProperty:forKey:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Changes the specified property of the receiver’s resource.

**Availability**:
- macOS 10.0+ - Deprecated in 10.4

## Declaration

```objc
- (BOOL) setProperty:(id) property forKey:(NSString *) propertyKey;
```

## Return Value

Returns [`true`](../../Swift/true.md) if the modification was successful, [`false`](../../Swift/false.md) otherwise.

## Parameters

- `property`: The new value of the property of the receiver’s resource.
- `propertyKey`: The key of the desired property.

## See Also

### Deprecated
- [convenience init?(scheme: String, host: String?, path: String)](./init%28scheme,host,path%29.md)
  Initializes a newly created NSURL with a specified scheme, host, and path.
- [- URLHandleUsingCache:](./urlhandleusingcache_.md)
  Returns a URL handle to service the receiver.
- [- loadResourceDataNotifyingClient:usingCache:](./loadresourcedatanotifyingclient_usingcache_.md)
  Loads the receiver’s resource data in the background.
- [- resourceDataUsingCache:](./resourcedatausingcache_.md)
  Returns the receiver’s resource data, loading it if necessary.
- [- setResourceData:](./setresourcedata_.md)
  Attempts to set the resource data for the receiver.
- [- propertyForKey:](./propertyforkey_.md)
  Returns the specified property of the receiver’s resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/setproperty:forkey:)*