# rotationOnYAxis

**Framework**: ARKit  
**Kind**: property

A radian value that indicates a plane’s y-axis orientation.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
var rotationOnYAxis: Float { get }
```

#### Discussion

As the session runs, the framework may update the plane’s y-rotation to better fit its rectangular area in the environment. In iOS 15 and earlier, the framework rotates the plane anchor according to that angle. In iOS 16, the framework doesn’t rotate the anchor automatically and its transform matrix remains unchanged. Instead, the framework exposes the angle in [`rotationOnYAxis`](arplaneextent/rotationonyaxis.md) that you apply to any plane extent geometry in your app.

> ❗ **Important**:  Apps that run on iOS 16 with a deployment target less than iOS 16 preserve the prior y-axis rotation behavior.

 Apps that run on iOS 16 with a deployment target less than iOS 16 preserve the prior y-axis rotation behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arplaneextent/rotationonyaxis)*