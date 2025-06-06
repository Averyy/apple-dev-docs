# isEqualTo

**Framework**: DriverKit  
**Kind**: method

Compares the array with an OSObject

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

True iff the object is of class OSArray and isEqualTo(const OSArray * anArray) returns true.

#### Discussion

If the object is of class OSArray, the result of isEqualTo(const OSArray * anArray) is returned. Otherwise false is returned.

## Parameters

- `anObject`: The object to compare with.

## See Also

- [isEqualTo](osarray/isequalto-5w7om.md)
  Compares all members of two arrays with isEqualTo().


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osarray/isequalto-93qxy)*