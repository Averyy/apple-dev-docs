# compare(_:)

**Framework**: Core Spotlight  
**Kind**: method  
**Role**: Instance Method

Compares the suggestion with a second specified suggestion.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func compare(_ other: CSSuggestion) -> ComparisonResult
```

```objc
- (NSComparisonResult) compare:(CSSuggestion *) other;
```

#### Return Value

Returns an `NSComparisonResult`.

## Parameters

- `other`: The suggestion to compare to this suggestion.

## See Also

### Comparing suggestions
- [func compare(byRank: CSSuggestion) -> ComparisonResult](./compare%28byrank%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssuggestion/compare(_:))*