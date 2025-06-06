# ensureCapacity

**Framework**: DriverKit  
**Kind**: method

Allocates capacity for members in dictionary.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
uint32_t ensureCapacity(uint32_t newCapacity);
```

#### Return Value

New count of capacity for members in dictionary, may return prior capacity on failure.

## Parameters

- `newCapacity`: Count of allocated capacity for members in dictionary.

## See Also

- [getCapacity](osdictionary/getcapacity.md)
  Returns count of currently allocated capacity for members in dictionary.
- [getCount](osdictionary/getcount.md)
  Returns count of members in dictionary.
- [OSDictionaryGetCount](osdictionarygetcount.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osdictionary/ensurecapacity)*