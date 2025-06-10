# init(_:rounded:)

**Framework**: Core Video  
**Kind**: init

Convert `CGSize` to [`CVImageSize`](cvimagesize.md) using the given rounding rule.

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
init(_ size: CGSize, rounded rule: FloatingPointRoundingRule = .down)
```

#### Discussion

The same rounding rule is applied to both height and width.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvimagesize/init(_:rounded:))*