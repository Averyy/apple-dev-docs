# exposureOffset

**Framework**: ARKit  
**Kind**: property

A value you supply to your custom renderer to light your scene.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var exposureOffset: Float { get }
```

#### Discussion

If your app displays an AR experience using a custom Metal renderer, use this value to light your scene during its post-processed lighting stage.

Lighting a scene using [`exposureOffset`](arcamera/exposureoffset.md) is normally more performant than scaling each light source in your scene based on the value of the frame’s [`lightEstimate`](arframe/lightestimate.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcamera/exposureoffset)*