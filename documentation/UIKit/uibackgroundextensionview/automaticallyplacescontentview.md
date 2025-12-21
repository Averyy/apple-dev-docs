# automaticallyPlacesContentView

**Framework**: UIKit  
**Kind**: property

Controls the automatic safe area placement of the `contentView` within the container.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

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