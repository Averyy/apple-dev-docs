# maximumSupportedContentVersion

**Framework**: PencilKit  
**Kind**: property

The maximum version of PencilKit to support.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var maximumSupportedContentVersion: PKContentVersion { get set }
```

#### Discussion

The default value is [`latest`](pkcontentversion/latest.md).

If you set this property to a value less than [`latest`](pkcontentversion/latest.md), the canvas view limits the edits that a person can make so they’re compatible with the version of PencilKit you specify.

If you set this property, also set [`maximumSupportedContentVersion`](pktoolpicker/maximumsupportedcontentversion.md) on any [`PKToolPicker`](pktoolpicker.md) you use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkcanvasview/maximumsupportedcontentversion)*