# isEqualTo

**Framework**: DriverKit  
**Kind**: method

Compares the string with an OSObject

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
bool isEqualTo(const OSMetaClassBase * anObject) const;
```

#### Return Value

True iff the object is of class OSData or OSString and isEqualTo() returns true.

#### Discussion

If the object is of class OSString, the result of isEqualTo(const OSString * aDataObj) is returned. If the object is of class OSData, the result of isEqualTo(const OSData * aDataObj) is returned. Otherwise false is returned.

## Parameters

- `anObject`: The object to compare with.

## See Also

- [isEqualTo](osstring/isequalto-1uq1f.md)
  Compares the string with an OSData.
- [isEqualTo](osstring/isequalto-5paj5.md)
  Compares the string with an OSString.
- [isEqualTo](osstring/isequalto-2rg80.md)
  Compares the string with a c-string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osstring/isequalto-712xj)*