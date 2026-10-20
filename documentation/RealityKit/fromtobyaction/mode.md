# mode

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

Determines the entities transform [`from`](./from.md) and [`to`](./to.md) are relative to.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
var mode: FromToByAction<Transform>.TransformMode? { get }
```

Available when `Value` is `Transform`.

#### Discussion

> **Note**: The expection to this mode is `by`. This property is relative to the starting value, Set this to `nil` if only `by` is specified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/fromtobyaction/mode)*