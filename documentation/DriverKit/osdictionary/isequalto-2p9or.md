# isEqualTo

**Framework**: DriverKit  
**Kind**: method

Compares certain members of two dictionaries with isEqualTo().

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
bool isEqualTo(const OSDictionary * aDictionary, const OSCollection * keys) const;
```

#### Return Value

True if both dictionaries have equal counts, every key exists in both, values for each key compare true with isEqualTo().

#### Discussion

For each key in the given collection, both dictionaries must contain values for the key that compare successfully with isEqualTo().

## Parameters

- `aDictionary`: The other dictionary to compare with.
- `keys`: The collection of keys to compare.

## See Also

- [isEqualTo](osdictionary/isequalto-3c1k0.md)
  Compares all members of two dictionaries with isEqualTo().
- [isEqualTo](osdictionary/isequalto-3kuk7.md)
  Compares the dictionary with an OSObject


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osdictionary/isequalto-2p9or)*