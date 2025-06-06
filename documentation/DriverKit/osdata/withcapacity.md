# withCapacity

**Framework**: DriverKit  
**Kind**: method

Allocates an OSData object with preallocated capacity.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
static OSDataPtr withCapacity(uint32_t capacity);
```

#### Return Value

NULL on failure, otherwise the allocated OSData with reference count 1 to be released by the caller.

#### Discussion

Allocates an OSData object with preallocated capacity. The OSData will have zero length until data is added to it with appendBytes().

## Parameters

- `capacity`: Number of bytes of data the object can hold.

## See Also

- [withBytes](osdata/withbytes.md)
  Allocates an OSData object with a copy of bytes.
- [withBytesNoCopy](osdata/withbytesnocopy.md)
  Allocates an OSData object with a copy of bytes.
- [withData](osdata/withdata-9y3g.md)
  Allocates an OSData object with a copy of bytes from another OSData.
- [withData](osdata/withdata-4rd8n.md)
  Allocates an OSData object with a copy of bytes from a subset of another OSData.
- [OSDataCreate](osdatacreate.md)
- [OSDataPtr](osdataptr.md)
- [free](osdata/free.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osdata/withcapacity)*