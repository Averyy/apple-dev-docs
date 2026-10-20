# isInputMuted

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the app’s audio input is in a muted state.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 26.0+
- watchOS 10.0+

## Declaration

```swift
var isInputMuted: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isInputMuted) BOOL inputMuted;
```

#### Discussion

Set a new value for this property by calling the [`setInputMuted(_:)`](./setinputmuted%28_%29.md) method.

## See Also

### Managing audio input mute state
- [func setInputMuted(Bool) throws](./setinputmuted%28_%29.md)
  Sets a Boolean value that indicates whether the app’s audio input is in a muted state.
- [class let inputMuteStateChangeNotification: NSNotification.Name](./inputmutestatechangenotification.md)
  A notification the system posts when the app’s audio input mute state changes.
- [func setInputMuteStateChangeHandler(((Bool) -> Bool)?) throws](./setinputmutestatechangehandler%28_%29.md)
  Sets a callback to handle changes to application-level audio muting states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioapplication/isinputmuted)*