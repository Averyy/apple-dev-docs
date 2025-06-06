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
const void * getBytesNoCopy() const;
```

#### Return Value

A pointer to the data or NULL if the OSData has zero length.

## See Also

- [getBytesNoCopy](osdata/getbytesnocopy-53puz.md)
  Returns a pointer to the OSData object’s internal data buffer.
- [OSDataGetBytes](osdatagetbytes.md)
- [OSDataGetBytesPtr](osdatagetbytesptr.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osdata/getbytesnocopy-91vcg)*