# present(launchConfiguration:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Launches Desk View with the configuration and completion handler that you specify.

**Availability**:
- Mac Catalyst 16.1+
- macOS 13.0+

## Declaration

```swift
func present(launchConfiguration: AVCaptureDeskViewApplication.LaunchConfiguration) async throws
```

#### Discussion

If Desk View is already running, this method brings it to the front. If Desk View is in the Dock, this method opens it and brings it to the front.

Desk View launches in setup mode. This mode shows the full field of view of an ultrawide camera with a superimposed trapezoid that indicates the cropped desk region to display. The system displays this region after the user completes setup and starts Desk View.

Create an instance of [`AVCaptureDeskViewApplication.LaunchConfiguration`](avcapturedeskviewapplication/launchconfiguration.md) and set it for `launchConfiguration` to specify the frame for Desk View and when to perform the `completionHandler`.

## Parameters

- `launchConfiguration`: A configuration that specifies how to present Desk View.
- `completionHandler`: The code to perform after the system displays Desk View or the user transitions to Desk View after setup, depending on the configuration.

## See Also

- [func present(completionHandler: (((any Error)?) -> Void)?)](avcapturedeskviewapplication/present(completionhandler:).md)
  Launches Desk View with no additional configuration and then performs a completion handler if you specify it.
- [AVCaptureDeskViewApplication.LaunchConfiguration](avcapturedeskviewapplication/launchconfiguration.md)
  An object that configures how to present Desk View.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedeskviewapplication/present(launchconfiguration:completionhandler:))*