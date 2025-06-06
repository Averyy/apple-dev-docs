# commands

**Framework**: AppKit  
**Kind**: property

An array of strings defining the commands for which the speech recognizer object should listen.

**Availability**:
- macOS ?+

## Declaration

```swift
var commands: [String]? { get set }
```

#### Discussion

Setting this property when the speech recognizer is already listening means that the current command list is updated and listening continues. The items in the array should be [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) objects. The command strings must match the current locale of the recognizer, which is selected in the Dictation pane of Accessibility system preferences.

## See Also

- [var displayedCommandsTitle: String?](nsspeechrecognizer/displayedcommandstitle.md)
  The title of the commands section in the Speech Commands window or `nil` if there is no title.
- [var listensInForegroundOnly: Bool](nsspeechrecognizer/listensinforegroundonly.md)
  A Boolean value that indicates whether the speech recognizer object should only enable its commands when its application is the frontmost one.
- [var blocksOtherRecognizers: Bool](nsspeechrecognizer/blocksotherrecognizers.md)
  A Boolean value that indicates whether the speech recognizer object should block all other recognizers (that is, other applications attempting to understand spoken commands) when listening.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechrecognizer/commands)*