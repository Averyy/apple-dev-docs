# mode

**Framework**: RealityKit  
**Kind**: property

Determines the entities transform [`from`](fromtobyaction/from.md) and [`to`](fromtobyaction/to.md) are relative to.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
var mode: FromToByAction<Transform>.TransformMode? { get }
```

#### Discussion

> **Note**: The expection to this mode is `by`. This property is relative to the starting value, Set this to `nil` if only `by` is specified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/fromtobyaction/mode)*