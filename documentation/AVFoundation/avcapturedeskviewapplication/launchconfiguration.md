# AVCaptureDeskViewApplication.LaunchConfiguration

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

An object that configures how to present Desk View.

**Availability**:
- Mac Catalyst 16.1+
- macOS 13.0+

## Declaration

```swift
class LaunchConfiguration
```

```objc
@interface AVCaptureDeskViewApplicationLaunchConfiguration : NSObject
```

## Overview

Use this object to specify the frame for Desk View when it launches, and when to execute the completion handler. You can specify whether to perform the completion handler as soon as Desk View is visible to the user, or only after they start Desk View.

## Topics

### Customizing the presentation
- [var mainWindowFrame: CGRect](./launchconfiguration/mainwindowframe.md)
  The frame for Desk View after it launches.
- [var requiresSetUpModeCompletion: Bool](./launchconfiguration/requiressetupmodecompletion.md)
  A Boolean value that specifies whether the system requires the user to complete setup mode before it executes the completion handler.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)

## See Also

### Presenting the Desk View app
- [func present(completionHandler: (((any Error)?) -> Void)?)](./present%28completionhandler%29.md)
  Launches Desk View with no additional configuration and then performs a completion handler if you specify it.
- [func present(launchConfiguration: AVCaptureDeskViewApplication.LaunchConfiguration, completionHandler: (((any Error)?) -> Void)?)](./present%28launchconfiguration,completionhandler%29.md)
  Launches Desk View with the configuration and completion handler that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedeskviewapplication/launchconfiguration)*