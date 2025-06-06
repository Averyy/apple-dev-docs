# isInputMuted

**Framework**: AVFAudio  
**Kind**: property

A Boolean value that indicates whether the app’s audio input is in a muted state.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
var isInputMuted: Bool { get }
```

#### Discussion

Set a new value for this property by calling the [`setInputMuted(_:)`](avaudioapplication/setinputmuted(_:).md) method.

## See Also

- [func setInputMuted(Bool) throws](avaudioapplication/setinputmuted(_:).md)
  Sets a Boolean value that indicates whether the app’s audio input is in a muted state.
- [class let inputMuteStateChangeNotification: NSNotification.Name](avaudioapplication/inputmutestatechangenotification.md)
  A notification the system posts when the app’s audio input mute state changes.
- [func setInputMuteStateChangeHandler(((Bool) -> Bool)?) throws](avaudioapplication/setinputmutestatechangehandler(_:).md)
  Sets a callback to handle changes to application-level audio muting states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioapplication/isinputmuted)*