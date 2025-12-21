# init(_:rounded:)

**Framework**: Core Video  
**Kind**: init

Convert `CGSize` to [`CVImageSize`](cvimagesize.md) using the given rounding rule.

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
init(_ size: CGSize, rounded rule: FloatingPointRoundingRule = .down)
```

#### Discussion

The same rounding rule is applied to both height and width.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvimagesize/init(_:rounded:))*