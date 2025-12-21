# byteCount

**Framework**: Swift  
**Kind**: property

The number of bytes in the span.

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 12.2+
- macOS 10.14.4+
- tvOS 12.2+
- visionOS 1.0+
- watchOS 5.2+

## Declaration

```swift
var byteCount: Int { get }
```

#### Discussion

To check whether the span is empty, use its `isEmpty` property instead of comparing `count` to zero.

> **Note**: O(1)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/rawspan/bytecount)*