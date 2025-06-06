# filter(matchingCategory:)

**Framework**: Swift  
**Kind**: method

Filters a sequence of tags based on matching the specified category.  Returns the tags that match the specified category.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func filter<T>(matchingCategory category: CMTypedTag<T>.Category) -> [CMTypedTag<T>] where T : Sendable
```

#### Discussion

- category: The category to match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/sequence/filter(matchingcategory:))*