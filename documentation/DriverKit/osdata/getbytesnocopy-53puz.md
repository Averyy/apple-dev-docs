# getBytesNoCopy

**Framework**: DriverKit  
**Kind**: method

Returns a pointer to the OSData object’s internal data buffer.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
const void * getBytesNoCopy(size_t start, size_t numBytes) const;
```

#### Return Value

A pointer to the data or NULL if the OSData does not have data for all the requested range.

## Parameters

- `start`: An offset into the OSData object.
- `numBytes`: The length of data intended to be read. If (start + numBytes) exceeds the size of the OSData’s length, the call will fail.

## See Also

- [getBytesNoCopy](osdata/getbytesnocopy-91vcg.md)
  Returns a pointer to the OSData object’s internal data buffer.
- [OSDataGetBytes](osdatagetbytes.md)
- [OSDataGetBytesPtr](osdatagetbytesptr.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osdata/getbytesnocopy-53puz)*