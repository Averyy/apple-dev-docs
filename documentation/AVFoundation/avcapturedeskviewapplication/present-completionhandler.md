# present(completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Launches Desk View with no additional configuration and then performs a completion handler if you specify it.

**Availability**:
- Mac Catalyst 16.1+
- macOS 13.0+

## Declaration

```swift
func present() async throws
```

#### Discussion

If the Desk View app is already running, this method brings it to the front. If Desk View is in the Dock, this method opens it and brings it to the front.

Desk View launches in setup mode. This mode shows the full field of view of an ultrawide camera with a superimposed trapezoid that indicates the cropped desk region to display. The system displays this region after the user completes setup and starts Desk View.

## Parameters

- `completionHandler`: The code to perform after the system displays Desk View.

## See Also

- [func present(launchConfiguration: AVCaptureDeskViewApplication.LaunchConfiguration, completionHandler: (((any Error)?) -> Void)?)](avcapturedeskviewapplication/present(launchconfiguration:completionhandler:).md)
  Launches Desk View with the configuration and completion handler that you specify.
- [AVCaptureDeskViewApplication.LaunchConfiguration](avcapturedeskviewapplication/launchconfiguration.md)
  An object that configures how to present Desk View.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedeskviewapplication/present(completionhandler:))*