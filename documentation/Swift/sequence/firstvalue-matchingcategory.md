# firstValue(matchingCategory:)

**Framework**: Swift  
**Kind**: method

Finds the first tag matching the specified category and returns the value of the matching tag.

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
func firstValue<T>(matchingCategory category: CMTypedTag<T>.Category) -> T? where T : Sendable
```

#### Discussion

- category: The category to match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/sequence/firstvalue(matchingcategory:))*