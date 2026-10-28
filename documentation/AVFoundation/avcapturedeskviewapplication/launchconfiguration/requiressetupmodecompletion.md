# requiresSetUpModeCompletion

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that specifies whether the system requires the user to complete setup mode before it executes the completion handler.

**Availability**:
- Mac Catalyst 16.1+
- macOS 13.0+

## Declaration

```swift
var requiresSetUpModeCompletion: Bool { get set }
```

```objc
@property BOOL requiresSetUpModeCompletion;
```

## Discussion

The default value is [`false`](../../../Swift/false.md), which tells the system to execute the completion handler as soon as it displays Desk View. If [`true`](../../../Swift/true.md), the system executes the completion handler after the user completes setup and starts Desk View.

## See Also

### Customizing the presentation
- [var mainWindowFrame: CGRect](./mainwindowframe.md)
  The frame for Desk View after it launches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedeskviewapplication/launchconfiguration/requiressetupmodecompletion)*