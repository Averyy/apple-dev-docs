# isEqualTo

**Framework**: DriverKit  
**Kind**: method

Compares the dictionary with an OSObject

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

True iff the object is of class OSDictionary and isEqualTo(const OSDictionary * anArray) returns true.

#### Discussion

If the object is of class OSDictionary, the result of isEqualTo(const OSDictionary * anArray) is returned. Otherwise false is returned.

## Parameters

- `anObject`: The object to compare with.

## See Also

- [isEqualTo](osdictionary/isequalto-3c1k0.md)
  Compares all members of two dictionaries with isEqualTo().
- [isEqualTo](osdictionary/isequalto-2p9or.md)
  Compares certain members of two dictionaries with isEqualTo().


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osdictionary/isequalto-3kuk7)*