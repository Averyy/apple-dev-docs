# getBytesNoCopy

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

Returns a pointer to the OSData object’s internal data buffer.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
const void * getBytesNoCopy() const;
```

## Return Value

A pointer to the data or NULL if the OSData has zero length.

## See Also

### Getting Bytes
- [getBytesNoCopy](./getbytesnocopy-53puz.md)
  Returns a pointer to the OSData object’s internal data buffer.
- [OSDataGetBytes](../osdatagetbytes.md)
- [OSDataGetBytesPtr](../osdatagetbytesptr.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osdata/getbytesnocopy-91vcg)*