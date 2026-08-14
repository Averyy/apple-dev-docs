# blocksOtherRecognizers

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the speech recognizer object should block all other recognizers (that is, other applications attempting to understand spoken commands) when listening.

**Availability**:
- macOS ?+

## Declaration

```swift
var blocksOtherRecognizers: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), all other speech recognition commands on the system are disabled until the speech recognizer is released, listening is stopped, or the property is set to [`false`](https://developer.apple.com/documentation/swift/false). Setting this property to [`true`](https://developer.apple.com/documentation/swift/true) effectively takes over the computer at the expense of other applications using speech recognition, so you should use it only in circumstances that warrant it, such as when listening for a response important to overall system operation or when an application is running in full-screen mode (such as games and presentation software). The default is value of this property is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var commands: [String]?](nsspeechrecognizer/commands.md)
  An array of strings defining the commands for which the speech recognizer object should listen.
- [var displayedCommandsTitle: String?](nsspeechrecognizer/displayedcommandstitle.md)
  The title of the commands section in the Speech Commands window or `nil` if there is no title.
- [var listensInForegroundOnly: Bool](nsspeechrecognizer/listensinforegroundonly.md)
  A Boolean value that indicates whether the speech recognizer object should only enable its commands when its application is the frontmost one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechrecognizer/blocksotherrecognizers)*