# isEqualTo

**Framework**: DriverKit  
**Kind**: method

Compares the number with an OSNumber.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
bool isEqualTo(const OSNumber * aNumber) const;
```

#### Return Value

True iff the two numbers have the same value.

#### Discussion

If the passed OSNumber object has the same value, regardless of size, true is returned. Otherwise false is returned.

## Parameters

- `aNumber`: The OSNumber to compare with.

## See Also

- [isEqualTo](osnumber/isequalto-333kh.md)
  Compares the string with an OSObject


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osnumber/isequalto-58rb9)*