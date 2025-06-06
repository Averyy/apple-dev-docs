# showsLargeContentViewer

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

A Boolean value that indicates whether or not to show the item in the large content viewer.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var showsLargeContentViewer: Bool { get }
```

#### Discussion

For this property to take effect, the item or an ancestor view must have a [`UILargeContentViewerInteraction`](uilargecontentviewerinteraction.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilargecontentvieweritem/showslargecontentviewer)*