# includeChildWindows

**Framework**: ScreenCaptureKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that specifies whether the screenshot captures subwindows of the included apps and windows.

**Availability**:
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
var includeChildWindows: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL includeChildWindows;
```

#### Discussion

By default taking a screenshot captures subwindows. For example, alerts, popovers, and sheets are captured by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scscreenshotconfiguration/includechildwindows)*