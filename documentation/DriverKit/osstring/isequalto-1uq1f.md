# isEqualTo

**Framework**: DriverKit  
**Kind**: method

Compares the string with an OSData.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
bool isEqualTo(const OSData * aDataObject) const;
```

#### Return Value

True if the OSData and OSString contain the same c-string.

#### Discussion

If the passed OSData object has the same length and all bytes are identical, true is returned. If the passed OSData object has a length one byte greater than the OSString, all bytes are identical, and the last byte of the OSData is zero, true is returned. Otherwise false is returned.

## Parameters

- `aDataObject`: The OSData to compare with.

## See Also

- [isEqualTo](osstring/isequalto-712xj.md)
  Compares the string with an OSObject
- [isEqualTo](osstring/isequalto-5paj5.md)
  Compares the string with an OSString.
- [isEqualTo](osstring/isequalto-2rg80.md)
  Compares the string with a c-string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osstring/isequalto-1uq1f)*