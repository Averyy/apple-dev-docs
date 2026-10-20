# isEqualTo

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

Compares the data with a pointer to bytes

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
bool isEqualTo(const void *bytes, size_t numBytes) const;
```

#### Return Value

True iff the length of the data are equal and all bytes are identical.

#### Discussion

If the passed data has the same length and all bytes are identical, true is returned. Otherwise false is returned.

## Parameters

- `bytes`: C-pointer to untyped data.
- `numBytes`: Count of bytes to be compared.

## See Also

### Comparing Data Objects
- [isEqualTo](./isequalto-2kdml.md)
  Compares the data with an OSData
- [isEqualTo](./isequalto-4xz0j.md)
  Compares the data with an OSObject
- [isEqualTo](./isequalto-5ssf5.md)
  Compares the data with an OSString


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osdata/isequalto-79gqy)*