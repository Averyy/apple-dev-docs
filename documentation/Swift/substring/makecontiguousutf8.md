# makeContiguousUTF8()

**Framework**: Swift  
**Kind**: method

If this string is not contiguous, make it so. If this mutates the substring, it will invalidate any pre-existing indices.

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
mutating func makeContiguousUTF8()
```

#### Discussion

Complexity: O(n) if non-contiguous, O(1) if already contiguous


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/substring/makecontiguousutf8())*