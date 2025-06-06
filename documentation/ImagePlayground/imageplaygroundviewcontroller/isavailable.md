# isAvailable

**Framework**: Image Playground  
**Kind**: property

A Boolean value that indicates whether image generation is available on the current device.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+
- Mac Catalyst 18.1+
- macOS 15.1+
- visionOS 2.4+

## Declaration

```swift
@MainActor
@objc(available) @preconcurrency dynamic class var isAvailable: Bool { get }
```

#### Discussion

The value of this property is `true` when the current device supports image generation. A device might not support this feature if the device or system doesn’t have the resources necessary to generate the images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imageplaygroundviewcontroller/isavailable)*