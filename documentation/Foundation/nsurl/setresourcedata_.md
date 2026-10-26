# setResourceData:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Attempts to set the resource data for the receiver.

**Availability**:
- macOS 10.0+ - Deprecated in 10.4

## Declaration

```objc
- (BOOL) setResourceData:(NSData *) data;
```

#### Return Value

Returns [`true`](../../Swift/true.md) if successful, [`false`](../../Swift/false.md) otherwise.

#### Discussion

In the case of a file URL, setting the data involves writing `data` to the specified file.

## Parameters

- `data`: The data to set for the URL.

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
- [- propertyForKey:](./propertyforkey_.md)
  Returns the specified property of the receiver’s resource.
- [- setProperty:forKey:](./setproperty_forkey_.md)
  Changes the specified property of the receiver’s resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/setresourcedata:)*