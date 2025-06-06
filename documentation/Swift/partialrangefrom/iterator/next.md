# next()

**Framework**: Swift  
**Kind**: method

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
mutating func next() -> Bound?
```

#### Return Value

The next element in the underlying sequence, if a next element exists; otherwise, `nil`.

#### Discussion

Once `nil` has been returned, all subsequent calls return `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/partialrangefrom/iterator/next())*