# localDragSession

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

The drag session that corresponds to this drop session, for in-app drag activities.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var localDragSession: (any UIDragSession)? { get }
```

#### Discussion

The local drag session is `nil` if the drag activity started in a different app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidropsession/localdragsession)*