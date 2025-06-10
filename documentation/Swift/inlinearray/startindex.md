# startIndex

**Framework**: Swift  
**Kind**: property

The position of the first element in a nonempty array.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
var startIndex: InlineArray<count, Element>.Index { get }
```

#### Discussion

If the array is empty, `startIndex` is equal to `endIndex`.

> **Note**: O(1)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/inlinearray/startindex)*