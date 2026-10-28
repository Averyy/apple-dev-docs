# isConstantColorEnabled

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, getter=isConstantColorEnabled) BOOL constantColorEnabled;
```

## Discussion

The default value is [`false`](../../Swift/false.md). Set the value to [`true`](../../Swift/true.md) to enable support for taking constant color photos. You can only enable constant color capture if the value of [`isConstantColorSupported`](./isconstantcolorsupported.md) is [`true`](../../Swift/true.md).

> **Note**:  Enabling constant color requires a lengthy reconfiguration of the capture pipeline. If you intend to capture constant color photos, set this property to [`true`](../../Swift/true.md) before calling [`startRunning()`](../avcapturesession/startrunning%28%29.md), or within [`beginConfiguration()`](../avcapturesession/beginconfiguration%28%29.md) and [`commitConfiguration()`](../avcapturesession/commitconfiguration%28%29.md) calls on a running capture session.

## See Also

### Configuring constant color
- [var isConstantColorSupported: Bool](./isconstantcolorsupported.md)
  A Boolean value that indicates whether a photo output supports constant color capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/isconstantcolorenabled)*