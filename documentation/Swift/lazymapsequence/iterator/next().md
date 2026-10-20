# next()

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Advances to the next element and returns it, or `nil` if no next element exists.

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
mutating func next() -> Element?
```

Available when `Base` conforms to `Sequence`.

#### Discussion

Once `nil` has been returned, all subsequent calls return `nil`.

> **Precondition**: `next()` has not been applied to a copy of `self` since the copy was made.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/lazymapsequence/iterator/next())*