# dashboardWindow

**Framework**: CarPlay  
**Kind**: property

The window that belongs to the dashboard scene.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+

## Declaration

```swift
@MainActor
var dashboardWindow: UIWindow { get }
```

#### Discussion

Use this property to access the window CarPlay creates for your dashboard scene. You draw your navigation app’s map content into this window for display in the dashboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptemplateapplicationdashboardscene/dashboardwindow)*