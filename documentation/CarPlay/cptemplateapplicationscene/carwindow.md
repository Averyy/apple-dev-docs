# carWindow

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The window that belongs to the scene.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var carWindow: CPWindow { get }
```

```objc
@property (nonatomic, strong, readonly, nonnull) CPWindow * carWindow;
```

## Discussion

Use this property to access the window CarPlay creates for your scene. Only navigation apps have access to that window, and use it to draw their map content. All other categories of apps must use templates exclusively to draw their user interfaces.

## See Also

### Accessing the Window
- [class CPWindow](../cpwindow.md)
  A window that displays its content on the CarPlay screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptemplateapplicationscene/carwindow)*