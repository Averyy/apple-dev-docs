# next()

**Framework**: Combine  
**Kind**: method

Produces the next element in the prefix sequence.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
mutating func next() async -> P.Output?
```

#### Return Value

The next published element, or nil if the publisher finishes normally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/asyncpublisher/iterator/next())*