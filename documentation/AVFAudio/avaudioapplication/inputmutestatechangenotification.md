# inputMuteStateChangeNotification

**Framework**: AVFAudio  
**Kind**: property

A notification the system posts when the app’s audio input mute state changes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 26.0+ (Beta)
- watchOS 10.0+

## Declaration

```swift
class let inputMuteStateChangeNotification: NSNotification.Name
```

## Topics

### User information keys
- [class let muteStateKey: String](avaudioapplication/mutestatekey.md)
  A user information key to determine the app’s audio mute state.

## See Also

- [var isInputMuted: Bool](avaudioapplication/isinputmuted.md)
  A Boolean value that indicates whether the app’s audio input is in a muted state.
- [func setInputMuted(Bool) throws](avaudioapplication/setinputmuted(_:).md)
  Sets a Boolean value that indicates whether the app’s audio input is in a muted state.
- [func setInputMuteStateChangeHandler(((Bool) -> Bool)?) throws](avaudioapplication/setinputmutestatechangehandler(_:).md)
  Sets a callback to handle changes to application-level audio muting states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioapplication/inputmutestatechangenotification)*