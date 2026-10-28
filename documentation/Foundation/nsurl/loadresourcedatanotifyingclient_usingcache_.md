# loadResourceDataNotifyingClient:usingCache:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Loads the receiver’s resource data in the background.

**Availability**:
- macOS 10.0+ - Deprecated in 10.4

## Declaration

```objc
- (void) loadResourceDataNotifyingClient:(id) client usingCache:(BOOL) shouldUseCache;
```

## Discussion

A given NSURL object can perform only one background load at a time.

### Special Considerations

Use the [`URLSession`](../urlsession.md) or [`NSURLConnection`](../nsurlconnection.md) classes for loading content from remote URLs.

## Parameters

- `client`: The client of the loading operation. `client` is notified of the receiver’s progress loading the resource data using the NSURLClient informal protocol. The NSURLClient messages are delivered on the current thread and require the run loop to be running.
- `shouldUseCache`: Whether the URL should use cached resource data from an already loaded URL that refers to the same resource. If `YES`, the cache is consulted when loading data. If `NO`, the data is always loaded directly, without consulting the cache.

## See Also

### Deprecated
- [convenience init?(scheme: String, host: String?, path: String)](./init%28scheme,host,path%29.md)
  Initializes a newly created NSURL with a specified scheme, host, and path.
- [- URLHandleUsingCache:](./urlhandleusingcache_.md)
  Returns a URL handle to service the receiver.
- [- resourceDataUsingCache:](./resourcedatausingcache_.md)
  Returns the receiver’s resource data, loading it if necessary.
- [- setResourceData:](./setresourcedata_.md)
  Attempts to set the resource data for the receiver.
- [- propertyForKey:](./propertyforkey_.md)
  Returns the specified property of the receiver’s resource.
- [- setProperty:forKey:](./setproperty_forkey_.md)
  Changes the specified property of the receiver’s resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/loadresourcedatanotifyingclient:usingcache:)*