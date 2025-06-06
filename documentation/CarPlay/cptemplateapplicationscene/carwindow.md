# carWindow

**Framework**: CarPlay  
**Kind**: property

The window that belongs to the scene.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var carWindow: CPWindow { get }
```

#### Discussion

Use this property to access the window CarPlay creates for your scene. Only navigation apps have access to that window, and use it to draw their map content. All other categories of apps must use templates exclusively to draw their user interfaces.

## See Also

- [class CPWindow](cpwindow.md)
  A window that displays its content on the CarPlay screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptemplateapplicationscene/carwindow)*