# isEqualTo

**Framework**: DriverKit  
**Kind**: method

Compares the data with an OSData

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
bool isEqualTo(const OSData * aDataObj) const;
```

#### Return Value

True iff the object is of class OSArray and isEqualTo(const OSArray * anArray) returns true.

#### Discussion

If the passed OSData object has the same length and all bytes are identical, true is returned. Otherwise false is returned.

## Parameters

- `aDataObj`: The OSData to compare with.

## See Also

- [isEqualTo](osdata/isequalto-4xz0j.md)
  Compares the data with an OSObject
- [isEqualTo](osdata/isequalto-5ssf5.md)
  Compares the data with an OSString
- [isEqualTo](osdata/isequalto-79gqy.md)
  Compares the data with a pointer to bytes


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osdata/isequalto-2kdml)*