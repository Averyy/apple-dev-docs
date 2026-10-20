# prepareRouteSelectionForPlayback(completionHandler:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Prepares the route selection for long-form video playback.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func prepareRouteSelectionForPlayback(completionHandler: @escaping @Sendable (Bool, AVAudioSession.RouteSelection) -> Void)
```

```swift
func prepareRouteSelectionForPlayback() async -> (Bool, AVAudioSession.RouteSelection)
```

```objc
- (void) prepareRouteSelectionForPlaybackWithCompletionHandler:(void (^)(BOOL shouldStartPlayback, AVAudioSessionRouteSelection routeSelection)) completionHandler;
```

#### Discussion

When playing long-form video content, call this method to indicate that playback is about to begin. Doing so provides the system the opportunity to prompt the user for an output destination, if needed, and perform any required routing.

The system only prompts the user to select a route if you’ve configured the audio session with a long-form video route-sharing policy. After the system configures the needed routing, it calls its completion handler, from which you can begin playback.

```swift
let session = AVAudioSession.sharedInstance()
session.prepareRouteSelectionForPlayback { shouldStartPlayback, routeSelection in
    if shouldStartPlayback {
        // Prepare and present player.
    }
}
```

## Parameters

- `completionHandler`: A completion handler called after the system finishes preparing the playback route. The system passes the completion handler the following parameters:

  - **`shouldStartPlayback`**: A Boolean value that indicates whether playback should start.
  - **`routeSelection`**: A route selection value that indicates the active playback route.

## See Also

### Related Documentation
- [func setCategory(AVAudioSession.Category, mode: AVAudioSession.Mode, policy: AVAudioSession.RouteSharingPolicy, options: AVAudioSession.CategoryOptions) throws](./setcategory%28_,mode,policy,options%29.md)
  Sets the session category, mode, route-sharing policy, and options.
### Preparing for long-form video playback
- [AVAudioSession.RouteSelection](./routeselection.md)
  Constants used to define the active route selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/preparerouteselectionforplayback(completionhandler:))*