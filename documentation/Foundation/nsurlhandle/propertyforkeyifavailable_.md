# propertyForKeyIfAvailable:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the property for the specified key only if the value is already available; that is, the client doesn’t need to do any work.

**Availability**:
- macOS 10.0+ - Deprecated in 10.4

> **Deprecated**: Use [`NSURLConnection`](../nsurlconnection.md) or [`NSURLDownload`](../nsurldownload.md) instead; see [URL Loading System](../url-loading-system.md).

## Declaration

```objc
- (id) propertyForKeyIfAvailable:(NSString *) propertyKey;
```

#### Return Value

The value associated with `propertyKey`. Returns `nil` if there is no such key or if the client would have to do work to fetch the property.

## Parameters

- `propertyKey`: The key of the desired property.

## See Also

### Setting and getting resource properties
- [- propertyForKey:](./propertyforkey_.md)
  Returns the property for the specified key.
- [- writeProperty:forKey:](./writeproperty_forkey_.md)
  Sets the property of the receiver’s resource for a specified key to the specified value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlhandle/propertyforkeyifavailable:)*