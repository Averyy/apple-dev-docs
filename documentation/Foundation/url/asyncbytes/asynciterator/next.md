# next()

**Framework**: Foundation  
**Kind**: method

Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.

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
mutating func next() async throws -> UInt8?
```

#### Return Value

The next element, if it exists, or `nil` to signal the end of the sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/asyncbytes/asynciterator/next())*