# AVCaptureDeskViewApplication.LaunchConfiguration

**Framework**: AVFoundation  
**Kind**: class

An object that configures how to present Desk View.

**Availability**:
- Mac Catalyst 16.1+
- macOS 13.0+

## Declaration

```swift
class LaunchConfiguration
```

#### Overview

Use this object to specify the frame for Desk View when it launches, and when to execute the completion handler. You can specify whether to perform the completion handler as soon as Desk View is visible to the user, or only after they start Desk View.

## Topics

### Customizing the presentation
- [var mainWindowFrame: CGRect](avcapturedeskviewapplication/launchconfiguration/mainwindowframe.md)
  The frame for Desk View after it launches.
- [var requiresSetUpModeCompletion: Bool](avcapturedeskviewapplication/launchconfiguration/requiressetupmodecompletion.md)
  A Boolean value that specifies whether the system requires the user to complete setup mode before it executes the completion handler.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func present(completionHandler: (((any Error)?) -> Void)?)](avcapturedeskviewapplication/present(completionhandler:).md)
  Launches Desk View with no additional configuration and then performs a completion handler if you specify it.
- [func present(launchConfiguration: AVCaptureDeskViewApplication.LaunchConfiguration, completionHandler: (((any Error)?) -> Void)?)](avcapturedeskviewapplication/present(launchconfiguration:completionhandler:).md)
  Launches Desk View with the configuration and completion handler that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedeskviewapplication/launchconfiguration)*