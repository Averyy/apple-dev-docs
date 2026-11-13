# floatingPointType

**Framework**: TabularData  
**Kind**: property  
**Role**: Instance Property

The type to use for floating-point numeric values.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var floatingPointType: CSVType
```

## Discussion

Defaults to [`CSVType.double`](../csvtype/double.md).

## See Also

### Interpreting values
- [var nilEncodings: Set<String>](./nilencodings.md)
  The set of strings that stores acceptable spellings for empty values.
- [var trueEncodings: Set<String>](./trueencodings.md)
  The set of strings that stores acceptable spellings for true Boolean values.
- [var falseEncodings: Set<String>](./falseencodings.md)
  The set of strings that stores acceptable spellings for false Boolean values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/csvreadingoptions/floatingpointtype)*