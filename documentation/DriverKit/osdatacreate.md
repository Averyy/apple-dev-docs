# OSDataCreate

**Framework**: DriverKit  
**Kind**: func

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
OSDataPtr OSDataCreate(const void * bytes, size_t length);
```

## See Also

- [withBytes](osdata/withbytes.md)
  Allocates an OSData object with a copy of bytes.
- [withBytesNoCopy](osdata/withbytesnocopy.md)
  Allocates an OSData object with a copy of bytes.
- [withCapacity](osdata/withcapacity.md)
  Allocates an OSData object with preallocated capacity.
- [withData](osdata/withdata-9y3g.md)
  Allocates an OSData object with a copy of bytes from another OSData.
- [withData](osdata/withdata-4rd8n.md)
  Allocates an OSData object with a copy of bytes from a subset of another OSData.
- [OSDataPtr](osdataptr.md)
- [free](osdata/free.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osdatacreate)*