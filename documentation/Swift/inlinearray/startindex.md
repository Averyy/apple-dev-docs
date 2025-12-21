# startIndex

**Framework**: Swift  
**Kind**: property

The position of the first element in a nonempty array.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var startIndex: InlineArray<count, Element>.Index { get }
```

#### Discussion

If the array is empty, `startIndex` is equal to `endIndex`.

> **Note**: O(1)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/inlinearray/startindex)*