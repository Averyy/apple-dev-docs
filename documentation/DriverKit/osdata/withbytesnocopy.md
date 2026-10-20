# withBytesNoCopy

**Framework**: DriverKit  
**Kind**: method  
**Role**: Static Method

Allocates an OSData object with a copy of bytes.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
static OSDataPtr withBytesNoCopy(void *bytes, size_t numBytes);
```

#### Return Value

NULL on failure, otherwise the allocated OSData with reference count 1 to be released by the caller.

#### Discussion

Allocates an OSData object with a copy of bytes. A synonym for OSData::withBytes() for compatibility with kernel code.

## Parameters

- `bytes`: C-pointer to untyped data. The data will be copied at the time of the call.
- `numBytes`: Count of bytes to be copied.

## See Also

### Creating a Data Object
- [withBytes](./withbytes.md)
  Allocates an OSData object with a copy of bytes.
- [withCapacity](./withcapacity.md)
  Allocates an OSData object with preallocated capacity.
- [withData](./withdata-9y3g.md)
  Allocates an OSData object with a copy of bytes from another OSData.
- [withData](./withdata-4rd8n.md)
  Allocates an OSData object with a copy of bytes from a subset of another OSData.
- [OSDataCreate](../osdatacreate.md)
- [OSDataPtr](../osdataptr.md)
- [free](./free.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osdata/withbytesnocopy)*