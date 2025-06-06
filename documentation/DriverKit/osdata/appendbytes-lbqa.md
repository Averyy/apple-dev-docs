# appendBytes

**Framework**: DriverKit  
**Kind**: method

Appends a buffer of bytes to the OSData object’s internal data buffer.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
bool appendBytes(const void * bytes, size_t numBytes);
```

#### Return Value

True on success or false on failure, due to allocation failure.

## Parameters

- `bytes`: C-pointer to untyped data. The data will be copied at the time of the call.
- `numBytes`: Count of bytes to be copied.

## See Also

- [appendBytes](osdata/appendbytes-38hs5.md)
  Appends a buffer of bytes to the OSData object’s internal data buffer.
- [OSDataAppendBytes](osdataappendbytes.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osdata/appendbytes-lbqa)*