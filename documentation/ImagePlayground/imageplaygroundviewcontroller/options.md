# options

**Framework**: Image Playground  
**Kind**: property

Options that influence the image-generation process.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- visionOS 26.4+

## Declaration

```swift
@MainActor
@preconcurrency var options: ImagePlaygroundOptions { get set }
```

#### Discussion

To specify custom options, modify the value in this property before you present the view controller. If you don’t modify this property, the view controller uses the default set of options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imageplaygroundviewcontroller/options)*