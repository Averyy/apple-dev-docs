# isEqualTo

**Framework**: DriverKit  
**Kind**: method

Compares all members of two arrays with isEqualTo().

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
bool isEqualTo(const OSArray * anArray) const;
```

#### Return Value

True if both arrays have equal counts and all members compare successfully with isEqualTo.

#### Discussion

If the arrays have equal counts, each member is compared with the other at the same index with isEqualTo(). Otherwise false is returned.

## Parameters

- `anArray`: The other array to compare with.

## See Also

- [isEqualTo](osarray/isequalto-93qxy.md)
  Compares the array with an OSObject


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osarray/isequalto-5w7om)*