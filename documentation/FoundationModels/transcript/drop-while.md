# drop(while:)

**Framework**: Foundation Models  
**Kind**: method

Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func drop(while predicate: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence
```

#### Discussion

> **Note**: O(), where  is the length of the collection.

## Parameters

- `predicate`: A closure that takes an element of the   sequence as its argument and returns   if the element should   be skipped or   if it should be included. Once the predicate   returns   it will not be called again.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/drop(while:))*