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

True iff the object is of class OSNumber isEqualTo() returns true.

#### Discussion

If the object is of class OSNumber, the result of isEqualTo(const OSNumber * aDataObj) is returned. Otherwise false is returned.

## Parameters

- `anObject`: The object to compare with.

## See Also

- [isEqualTo](osnumber/isequalto-58rb9.md)
  Compares the number with an OSNumber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osnumber/isequalto-333kh)*