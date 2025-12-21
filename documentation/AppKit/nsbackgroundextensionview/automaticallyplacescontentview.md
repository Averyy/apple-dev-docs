# automaticallyPlacesContentView

**Framework**: AppKit  
**Kind**: property

Controls the automatic safe area placement of the `contentView` within the container.

**Availability**:
- macOS 26.0+

## Declaration

```swift
@MainActor
var automaticallyPlacesContentView: Bool { get set }
```

#### Discussion

When `NO`, the frame of the content view must be explicitly set or constraints added. The extension effect will be used to fill the container view around the content.

Defaults to `YES`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbackgroundextensionview/automaticallyplacescontentview)*