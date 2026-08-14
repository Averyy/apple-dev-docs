# setCanControlQuickLookPanel(_:)

**Framework**: Quartz  
**Kind**: method

Specifies whether the view can automatically take control of the QuickLook panel.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func setCanControlQuickLookPanel(_ flag: Bool)
```

#### Discussion

When the browser view displays the QuickLook panel it sets itself as the QuickLook datasource. If the browser cells returned by the datasource return items that are URLs or paths, then the QuickLook panel will display the image at that location. Otherwise, the browser cell must implement the [`QLPreviewItem`](https://developer.apple.com/documentation/quicklook/qlpreviewitem) protocol and return the requested URL for the custom cell.

## Parameters

- `flag`: [`true`](https://developer.apple.com/documentation/swift/true), if the view can display the QuickLook panel, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [func canControlQuickLookPanel() -> Bool](ikimagebrowserview/cancontrolquicklookpanel.md)
  Returns whether the view can automatically take control of the QuickLook panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/setcancontrolquicklookpanel(_:))*