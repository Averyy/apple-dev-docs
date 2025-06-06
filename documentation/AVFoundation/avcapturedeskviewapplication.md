# AVCaptureDeskViewApplication

**Framework**: Avfoundation  
**Kind**: class

An object that programmatically presents Desk View.

**Availability**:
- Mac Catalyst 16.1+
- macOS 13.0+

## Declaration

```swift
class AVCaptureDeskViewApplication
```

#### Overview

Use this class to programmatically launch Desk View from your app. You can optionally customize the presentation and specifiy an action to take afterward.

> **Note**:  Desk View is available in iOS 16 and later on iPhone 11 and later, excluding iPhone SE, for use with a Mac running macOS 13 and later.

The following example shows how to configure and present Desk View with a completion handler:

```swift
let deskView = AVCaptureDeskViewApplication()
let configuration = AVCaptureDeskViewApplication.LaunchConfiguration()

// Use the previously set frame.
configuration.mainWindowFrame = .zero

// Execute the completion handler when the user starts Desk View.
configuration.requiresSetUpModeCompletion = true

// Launch Desk View with a configuration and completion handler.
deskView.present(launchConfiguration: configuration) { error in
    // Perform error handling and additional tasks.
}
```

## Topics

### Presenting the Desk View app
- [func present(completionHandler: (((any Error)?) -> Void)?)](avcapturedeskviewapplication/present(completionhandler:).md)
  Launches Desk View with no additional configuration and then performs a completion handler if you specify it.
- [func present(launchConfiguration: AVCaptureDeskViewApplication.LaunchConfiguration, completionHandler: (((any Error)?) -> Void)?)](avcapturedeskviewapplication/present(launchconfiguration:completionhandler:).md)
  Launches Desk View with the configuration and completion handler that you specify.
- [AVCaptureDeskViewApplication.LaunchConfiguration](avcapturedeskviewapplication/launchconfiguration.md)
  An object that configures how to present Desk View.

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

- [Supporting Continuity Camera in your tvOS app](../AVKit/supporting-continuity-camera-in-your-tvos-app.md)
  Capture high-quality photos, video, and audio in your Apple TV app by connecting an iPhone or iPad as a continuity device.
- [Supporting Continuity Camera in your macOS app](supporting-continuity-camera-in-your-macos-app.md)
  Enable high-quality photo and video capture by using an iPhone camera as an external capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AVFoundation/avcapturedeskviewapplication)*