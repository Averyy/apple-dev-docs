# setDisconnectedFromSystemAudio:completionHandler:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Changes whether the player is disconnected from system audio.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```objc
- (void) setDisconnectedFromSystemAudio:(BOOL) disconnected completionHandler:(void (^)()) completionHandler;
```

#### Discussion

This method allows you to dynamically change the player’s system audio connection. The operation is asynchronous. Each call to this method will invoke its own completion handler when the operation completes. When changing from NO to YES, you should typically call this method first, then deactivate the AVAudioSession in the completion handler to allow other audio to resume.

#### Using the completion handler

In a scenario where changing the value from NO to YES should also allow other system audio to resume, you should only deactivate the audio session once the player has disconnected from system audio.

```objective-c
// Disconnect from system audio and let other audio resume
[player setDisconnectedFromSystemAudio:YES completionHandler:^{
    [[AVAudioSession sharedInstance] setActive:NO withOptions:AVAudioSessionSetActiveOptionNotifyOthersOnDeactivation error:nil];
}];
```

## Parameters

- `disconnected`: YES to disconnect from system audio, NO to connect to it.
- `completionHandler`: A block that is called when the connection state change is complete. This block is called on an arbitrary queue. The completion handler may be nil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/setdisconnectedfromsystemaudio:completionhandler:)*