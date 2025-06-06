# isEqualTo

**Framework**: DriverKit  
**Kind**: method

Compares the data with an OSString

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
bool isEqualTo(const OSString * aString) const;
```

#### Return Value

True if the OSData and OSString contain the same c-string.

#### Discussion

If the passed OSString object has the same length and all bytes are identical, true is returned. If the passed OSString object has a length one byte less than the OSData, all bytes are identical, and the last byte of the OSData is zero, true is returned. Otherwise false is returned.

## Parameters

- `aString`: The object to compare with.

## See Also

- [isEqualTo](osdata/isequalto-2kdml.md)
  Compares the data with an OSData
- [isEqualTo](osdata/isequalto-4xz0j.md)
  Compares the data with an OSObject
- [isEqualTo](osdata/isequalto-79gqy.md)
  Compares the data with a pointer to bytes


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osdata/isequalto-5ssf5)*