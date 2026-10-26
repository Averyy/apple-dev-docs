# writeData:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Attempts to write a specified set of data to the location specified by the receiver’s URL.

**Availability**:
- macOS 10.0+ - Deprecated in 10.4

> **Deprecated**: Use [`NSURLConnection`](../nsurlconnection.md) or [`NSURLDownload`](../nsurldownload.md) instead; see [URL Loading System](../url-loading-system.md).

## Declaration

```objc
- (BOOL) writeData:(NSData *) data;
```

#### Return Value

[`true`](../../Swift/true.md) if successful, [`false`](../../Swift/false.md) otherwise.

#### Discussion

Must be overridden by subclasses.

## Parameters

- `data`: The data to write.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlhandle/writedata:)*