# progressIndicatorStyle

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

The drop-progress indicator style associated with the drop session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var progressIndicatorStyle: UIDropSessionProgressIndicatorStyle { get set }
```

#### Discussion

This property determines the type of progress indicator displayed when the drop operation takes a significant amount of time. The [`UIDropSessionProgressIndicatorStyle.default`](uidropsessionprogressindicatorstyle/default.md) style indicates that a progress indicator is shown by the system. If you prefer to show your own progress indicator, set this property to [`UIDropSessionProgressIndicatorStyle.none`](uidropsessionprogressindicatorstyle/none.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidropsession/progressindicatorstyle)*