# Strategy

**Framework**: Foundation  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

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
associatedtype Strategy : ParseStrategy where Self.FormatInput == Self.Strategy.ParseOutput, Self.FormatOutput == Self.Strategy.ParseInput
```

## See Also

### Declaring Parse Strategy
- [var parseStrategy: Self.Strategy](./parsestrategy.md)
  A `ParseStrategy` that can be used to parse this `FormatStyle`’s output


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/parseableformatstyle/strategy)*