# isEqualTo

**Framework**: DriverKit  
**Kind**: method

Compares the string with an OSString.

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

True iff the two strings have the same length and characters.

#### Discussion

If the passed OSString object has the same length and all characters are identical, true is returned. Otherwise false is returned.

## Parameters

- `aString`: The OSString to compare with.

## See Also

- [isEqualTo](osstring/isequalto-1uq1f.md)
  Compares the string with an OSData.
- [isEqualTo](osstring/isequalto-712xj.md)
  Compares the string with an OSObject
- [isEqualTo](osstring/isequalto-2rg80.md)
  Compares the string with a c-string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osstring/isequalto-5paj5)*