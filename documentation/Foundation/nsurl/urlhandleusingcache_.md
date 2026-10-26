# URLHandleUsingCache:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a URL handle to service the receiver.

**Availability**:
- macOS 10.0+ - Deprecated in 10.4

## Declaration

```objc
- (NSURLHandle *) URLHandleUsingCache:(BOOL) shouldUseCache;
```

#### Return Value

A URL handle to service the receiver.

#### Discussion

Sophisticated clients use the URL handle directly for additional control.

##### Special Considerations

Use the [`URLSession`](../urlsession.md) or [`NSURLConnection`](../nsurlconnection.md) classes for loading content from remote URLs.

## Parameters

- `shouldUseCache`: Whether to use a cached URL handle. If `shouldUseCache` is [`true`](../../Swift/true.md), the cache is searched for a URL handle that has serviced the receiver or another identical URL. If `shouldUseCache` is [`false`](../../Swift/false.md), a newly instantiated handle is returned, even if an equivalent URL has been loaded.

## See Also

### Related Documentation
- [+ cachedHandleForURL:](../nsurlhandle/cachedhandleforurl_.md)
  Returns the URL handle from the cache that has serviced the specified URL or another identical URL.
### Deprecated
- [convenience init?(scheme: String, host: String?, path: String)](./init%28scheme,host,path%29.md)
  Initializes a newly created NSURL with a specified scheme, host, and path.
- [- loadResourceDataNotifyingClient:usingCache:](./loadresourcedatanotifyingclient_usingcache_.md)
  Loads the receiver’s resource data in the background.
- [- resourceDataUsingCache:](./resourcedatausingcache_.md)
  Returns the receiver’s resource data, loading it if necessary.
- [- setResourceData:](./setresourcedata_.md)
  Attempts to set the resource data for the receiver.
- [- propertyForKey:](./propertyforkey_.md)
  Returns the specified property of the receiver’s resource.
- [- setProperty:forKey:](./setproperty_forkey_.md)
  Changes the specified property of the receiver’s resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/urlhandleusingcache:)*