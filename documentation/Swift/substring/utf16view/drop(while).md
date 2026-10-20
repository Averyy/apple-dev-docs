# drop(while:)

**Framework**: Swift  
**Kind**: method

Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func drop(while predicate: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence
```

#### Discussion

> **Note**: O(*n*), where *n* is the length of the collection.

## Parameters

- `predicate`: A closure that takes an element of the sequence as its argument and returns `true` if the element should be skipped or `false` if it should be included. Once the predicate returns `false` it will not be called again.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/substring/utf16view/drop(while:))*