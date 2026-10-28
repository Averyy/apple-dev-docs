# isEqualTo

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

Compares all members of two dictionaries with isEqualTo().

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
bool isEqualTo(const OSDictionary *aDictionary) const;
```

## Return Value

True if both dictionaries have equal counts, every key exists in both, values for each key compare true with isEqualTo().

## Discussion

If the dictionaries have equal counts, each member is compared with the other at the same index with isEqualTo(). Otherwise false is returned.

## Parameters

- `aDictionary`: The other dictionary to compare with.

## See Also

### Comparing Dictionaries
- [isEqualTo](./isequalto-2p9or.md)
  Compares certain members of two dictionaries with isEqualTo().
- [isEqualTo](./isequalto-3kuk7.md)
  Compares the dictionary with an OSObject


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osdictionary/isequalto-3c1k0)*