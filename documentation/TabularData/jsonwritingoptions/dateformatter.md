# dateFormatter

**Framework**: TabularData  
**Kind**: property  
**Role**: Instance Property

A closure that maps dates to their string representations.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var dateFormatter: (Date) -> String
```

## Discussion

Defaults to ISO 8601 encoding.

## See Also

### Formatting the JSON output
- [var prettyPrint: Bool](./prettyprint.md)
  A Boolean value that indicates whether to split lines and indent the generated JSON.
- [var sortKeys: Bool](./sortkeys.md)
  A Boolean value that indicates whether to sort the keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/jsonwritingoptions/dateformatter)*