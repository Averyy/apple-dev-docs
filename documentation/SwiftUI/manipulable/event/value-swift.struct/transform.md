# transform

**Framework**: SwiftUI  
**Kind**: property

The 3D affine transform of the manipulated view, or `nil` if the view doesn’t have a well-defined 3D affine transfrorm.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
let transform: AffineTransform3D?
```

#### Discussion

A view may not have a well-defined 3D affine transform e.g. when it’s affected by a projection transform.

This transform is in the coordinate space configured in the view modifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/manipulable/event/value-swift.struct/transform)*