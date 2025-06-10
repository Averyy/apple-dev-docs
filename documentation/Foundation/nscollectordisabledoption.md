# NSCollectorDisabledOption

**Framework**: Foundation  
**Kind**: var

Specifies that the block is retained, and therefore ineligible for collection. Specifying this option is equivalent to invoking [`disableCollectorForPointer:`](nsgarbagecollector/disablecollectorforpointer:.md) with the returned block as the argument.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var NSCollectorDisabledOption: Int { get }
```

## See Also

- [var NSScannedOption: Int](nsscannedoption.md)
  Specifies allocation of scanned memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscollectordisabledoption)*