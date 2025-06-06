# addDateParseStrategy(_:)

**Framework**: TabularData  
**Kind**: method

Adds a date parsing strategy.

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
mutating func addDateParseStrategy<T>(_ strategy: T) where T : ParseStrategy, T.ParseInput == String, T.ParseOutput == Date
```

## Parameters

- `strategy`: A parsing strategy that has a string input and a date output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/csvreadingoptions/adddateparsestrategy(_:))*