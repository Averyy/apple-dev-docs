# withData

**Framework**: DriverKit  
**Kind**: method

Allocates an OSData object with a copy of bytes from another OSData.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
static OSDataPtr withData(const OSData * inData);
```

#### Return Value

NULL on failure, otherwise the allocated OSData with reference count 1 to be released by the caller.

## Parameters

- `inData`: An OSData object to copy. The data will be copied at the time of the call.

## See Also

- [withBytes](osdata/withbytes.md)
  Allocates an OSData object with a copy of bytes.
- [withBytesNoCopy](osdata/withbytesnocopy.md)
  Allocates an OSData object with a copy of bytes.
- [withCapacity](osdata/withcapacity.md)
  Allocates an OSData object with preallocated capacity.
- [withData](osdata/withdata-4rd8n.md)
  Allocates an OSData object with a copy of bytes from a subset of another OSData.
- [OSDataCreate](osdatacreate.md)
- [OSDataPtr](osdataptr.md)
- [free](osdata/free.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osdata/withdata-9y3g)*