# trimmingPrefix(_:)

**Framework**: Swift  
**Kind**: method

Returns a subsequence of this collection by removing the elements matching the regex from the start, where the regex is created by the given closure.

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
func trimmingPrefix(@RegexComponentBuilder _ content: () -> some RegexComponent) -> Self.SubSequence
```

#### Return Value

A collection containing the elements after those that match the regex returned by `content`. If the regex does not match at the start of the collection, the entire contents of this collection are returned.

## Parameters

- `content`: A closure that returns the regex to search for at   the start of this collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/bidirectionalcollection/trimmingprefix(_:)-781ik)*