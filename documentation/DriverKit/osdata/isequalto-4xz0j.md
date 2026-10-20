# isEqualTo

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

Compares the data with an OSObject

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```cpp
virtual bool isEqualTo(const OSMetaClassBase *anObject) const;
```

#### Return Value

True iff the object is of class OSData or OSString and isEqualTo() returns true.

#### Discussion

If the object is of class OSData, the result of isEqualTo(const OSData * aDataObj) is returned. If the object is of class OSString, the result of OSString::isEqualTo(const OSData * aDataObj) is returned. Otherwise false is returned.

## Parameters

- `anObject`: The object to compare with.

## See Also

### Comparing Data Objects
- [isEqualTo](./isequalto-2kdml.md)
  Compares the data with an OSData
- [isEqualTo](./isequalto-5ssf5.md)
  Compares the data with an OSString
- [isEqualTo](./isequalto-79gqy.md)
  Compares the data with a pointer to bytes


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osdata/isequalto-4xz0j)*