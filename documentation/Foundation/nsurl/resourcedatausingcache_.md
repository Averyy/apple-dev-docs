# resourceDataUsingCache:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the receiver’s resource data, loading it if necessary.

**Availability**:
- macOS 10.0+ - Deprecated in 10.4

## Declaration

```objc
- (NSData *) resourceDataUsingCache:(BOOL) shouldUseCache;
```

## Return Value

The receiver’s resource data.

## Discussion

If the receiver has not already loaded its resource data, it will attempt to load it as a blocking operation.

In OS X v10.4, this method requests that the data be sent with gzip compression, however it does not automatically decompress the data if the server complies with this request. Data is automatically decompressed in macOS 10.5 and later.

### Special Considerations

Use the [`URLSession`](../urlsession.md) or [`NSURLConnection`](../nsurlconnection.md) classes for loading content from remote URLs.

## Parameters

- `shouldUseCache`: Whether the URL should use cached resource data from an already loaded URL that refers to the same resource. If `YES`, the cache is consulted when loading data. If `NO`, the data is always loaded directly, without consulting the cache.

## See Also

### Deprecated
- [convenience init?(scheme: String, host: String?, path: String)](./init%28scheme,host,path%29.md)
  Initializes a newly created NSURL with a specified scheme, host, and path.
- [- URLHandleUsingCache:](./urlhandleusingcache_.md)
  Returns a URL handle to service the receiver.
- [- loadResourceDataNotifyingClient:usingCache:](./loadresourcedatanotifyingclient_usingcache_.md)
  Loads the receiver’s resource data in the background.
- [- setResourceData:](./setresourcedata_.md)
  Attempts to set the resource data for the receiver.
- [- propertyForKey:](./propertyforkey_.md)
  Returns the specified property of the receiver’s resource.
- [- setProperty:forKey:](./setproperty_forkey_.md)
  Changes the specified property of the receiver’s resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/resourcedatausingcache:)*