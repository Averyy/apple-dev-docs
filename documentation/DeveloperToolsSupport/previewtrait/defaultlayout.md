# defaultLayout

**Framework**: DeveloperToolsSupport  
**Kind**: property

Center the preview in a container the size of the device on which the preview is running.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@MainActor
static var defaultLayout: PreviewTrait<Preview.ViewTraits> { get }
```

#### Discussion

This is the same as the [`PreviewLayout.device`](previewlayout/device.md) layout, and is the default if you don’t specify a layout trait.


---

*[View on Apple Developer](https://developer.apple.com/documentation/developertoolssupport/previewtrait/defaultlayout)*