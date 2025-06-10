# automaticallyPlacesContentView

**Framework**: UIKit  
**Kind**: property

Controls the automatic safe area placement of the `contentView` within the container.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
var automaticallyPlacesContentView: Bool { get set }
```

#### Discussion

When `NO`, the frame of the content view must be explicitly set or constraints added. The extension effect will be used to fill the container view around the content.

Defaults to `YES`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibackgroundextensionview/automaticallyplacescontentview)*