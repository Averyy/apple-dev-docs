# subdivision(for:)

**Framework**: Foundation  
**Kind**: method

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

#### Return Value

A subdivision that represents the entire region.

#### Discussion

For example, this method returns a subdivision with the `uszzzz` identifier for the entire US region.

## Parameters

- `region`: A region to represent as a subdivision.

## See Also

- [init(String)](locale/subdivision-swift.struct/init(_:).md)
  Creates a sudivision from a Unicode identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/subdivision-swift.struct/subdivision(for:))*