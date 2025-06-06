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
var maximumSupportedContentVersion: PKContentVersion { get set }
```

## Mentions

- [Supporting backward compatibility for ink types](supporting-backward-compatibility-for-ink-types.md)

#### Discussion

The default value is [`latest`](pkcontentversion/latest.md).

If you set this property to a value less than [`latest`](pkcontentversion/latest.md), the tool picker limits the tools that are available so they’re compatible with the version of PencilKit you specify.

If you set this property, also set [`maximumSupportedContentVersion`](pkcanvasview/maximumsupportedcontentversion.md) on the [`PKCanvasView`](pkcanvasview.md) you use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pktoolpicker/maximumsupportedcontentversion)*