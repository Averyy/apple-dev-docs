# carWindow

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The window that displays the scene’s content.

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

The system uses the scene’s window to manage its content. Navigation apps also use this window to display their custom map content. All other apps use a [`CPInterfaceController`](../cpinterfacecontroller.md) to present their interface content and don’t use this window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptemplateapplicationscene/carwindow)*