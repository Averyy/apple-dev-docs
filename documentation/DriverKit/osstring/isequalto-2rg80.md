# isEqualTo

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

Compares the string with a c-string.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
bool isEqualTo(const char *cString) const;
```

#### Return Value

True iff the two strings have the same length and characters.

#### Discussion

If the passed c-string has the same length and all characters are identical to those in the OSString, true is returned. Otherwise false is returned.

## Parameters

- `cString`: The c-string to compare with.

## See Also

### Comparing Strings
- [isEqualTo](./isequalto-1uq1f.md)
  Compares the string with an OSData.
- [isEqualTo](./isequalto-712xj.md)
  Compares the string with an OSObject
- [isEqualTo](./isequalto-5paj5.md)
  Compares the string with an OSString.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osstring/isequalto-2rg80)*