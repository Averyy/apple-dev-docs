# writeProperty:forKey:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sets the property of the receiver’s resource for a specified key to the specified value.

**Availability**:
- macOS 10.0+ - Deprecated in 10.4

> **Deprecated**: Use [`NSURLConnection`](../nsurlconnection.md) or [`NSURLDownload`](../nsurldownload.md) instead; see [URL Loading System](../url-loading-system.md).

## Declaration

```objc
- (BOOL) writeProperty:(id) propertyValue forKey:(NSString *) propertyKey;
```

## Return Value

[`true`](../../Swift/true.md) if the modification was successful, [`false`](../../Swift/false.md) otherwise.

## Discussion

Must be overridden by subclasses.

## Parameters

- `propertyValue`: The new value for the property.
- `propertyKey`: The key of the desired property.

## See Also

### Setting and getting resource properties
- [- propertyForKey:](./propertyforkey_.md)
  Returns the property for the specified key.
- [- propertyForKeyIfAvailable:](./propertyforkeyifavailable_.md)
  Returns the property for the specified key only if the value is already available; that is, the client doesn’t need to do any work.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlhandle/writeproperty:forkey:)*