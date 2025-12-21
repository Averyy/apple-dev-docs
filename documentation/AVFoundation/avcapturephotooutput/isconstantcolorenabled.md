# isConstantColorEnabled

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the photo output configures the render pipeline to perform constant color capture.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
var isConstantColorEnabled: Bool { get set }
```

#### Discussion

The default value is [`false`](https://developer.apple.com/documentation/Swift/false). Set the value to [`true`](https://developer.apple.com/documentation/Swift/true) to enable support for taking constant color photos. You can only enable constant color capture if the value of [`isConstantColorSupported`](avcapturephotooutput/isconstantcolorsupported.md) is [`true`](https://developer.apple.com/documentation/Swift/true).

> **Note**:  Enabling constant color requires a lengthy reconfiguration of the capture pipeline. If you intend to capture constant color photos, set this property to [`true`](https://developer.apple.com/documentation/Swift/true) before calling [`startRunning()`](avcapturesession/startrunning().md), or within [`beginConfiguration()`](avcapturesession/beginconfiguration().md) and [`commitConfiguration()`](avcapturesession/commitconfiguration().md) calls on a running capture session.

## See Also

- [var isConstantColorSupported: Bool](avcapturephotooutput/isconstantcolorsupported.md)
  A Boolean value that indicates whether a photo output supports constant color capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/isconstantcolorenabled)*