# bodyDetection

**Framework**: ARKit  
**Kind**: property

An option that indicates that 2D body detection is enabled.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
static var bodyDetection: ARConfiguration.FrameSemantics { get }
```

#### Discussion

When you set this option in your configuration’s [`frameSemantics`](arconfiguration/framesemantics-swift.property.md) property, ARKit describes the joint positions of a body it detects in the camera image, using normalized coordinates. See [`detectedBody`](arframe/detectedbody.md) for more information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arconfiguration/framesemantics-swift.struct/bodydetection)*