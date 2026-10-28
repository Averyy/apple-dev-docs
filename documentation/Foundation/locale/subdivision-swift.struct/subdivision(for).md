# subdivision(for:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns the subdivision representing the given region as a whole.

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
static func subdivision(for region: Locale.Region) -> Locale.Subdivision
```

## Return Value

A subdivision that represents the entire region.

## Discussion

For example, this method returns a subdivision with the `uszzzz` identifier for the entire US region.

## Parameters

- `region`: A region to represent as a subdivision.

## See Also

### Creating a subdivision
- [init(String)](./init%28_%29.md)
  Creates a sudivision from a Unicode identifier.
- [init(stringLiteral: String)](./init%28stringliteral%29.md)
  Creates a sudivision from a Unicode identifier as a string literal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/subdivision-swift.struct/subdivision(for:))*