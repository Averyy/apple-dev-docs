# portraitUpsideDown

**Framework**: DeveloperToolsSupport  
**Kind**: property  
**Role**: Type Property

The device is in portrait mode, but is upside down.

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
static var portraitUpsideDown: PreviewTrait<Preview.ViewTraits> { get }
```

Available when `T` is `Preview.ViewTraits`.

#### Discussion

This is the same as [`portraitUpsideDown`](../../SwiftUI/interfaceorientation/portraitupsidedown.md).

## See Also

### Getting an orientation
- [static var portrait: PreviewTrait<Preview.ViewTraits>](./portrait.md)
  The device is in portrait mode, with the top of the device on top.
- [static var landscapeLeft: PreviewTrait<Preview.ViewTraits>](./landscapeleft.md)
  The device is in landscape mode, with the top of the device on the left.
- [static var landscapeRight: PreviewTrait<Preview.ViewTraits>](./landscaperight.md)
  The device is in landscape mode, with the top of the device on the right.


---

*[View on Apple Developer](https://developer.apple.com/documentation/developertoolssupport/previewtrait/portraitupsidedown)*