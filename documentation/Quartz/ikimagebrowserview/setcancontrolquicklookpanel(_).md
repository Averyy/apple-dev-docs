# setCanControlQuickLookPanel(_:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Specifies whether the view can automatically take control of the QuickLook panel.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func setCanControlQuickLookPanel(_ flag: Bool)
```

```objc
- (void) setCanControlQuickLookPanel:(BOOL) flag;
```

#### Discussion

When the browser view displays the QuickLook panel it sets itself as the QuickLook datasource. If the browser cells returned by the datasource return items that are URLs or paths, then the QuickLook panel will display the image at that location. Otherwise, the browser cell must implement the [`QLPreviewItem`](../../QuickLook/qlpreviewitem.md) protocol and return the requested URL for the custom cell.

## Parameters

- `flag`: [`true`](../../Swift/true.md), if the view can display the QuickLook panel, otherwise [`false`](../../Swift/false.md).

## See Also

### QuickLook Support
- [func canControlQuickLookPanel() -> Bool](./cancontrolquicklookpanel%28%29.md)
  Returns whether the view can automatically take control of the QuickLook panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/setcancontrolquicklookpanel(_:))*