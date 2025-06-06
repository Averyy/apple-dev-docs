# displayedCommandsTitle

**Framework**: AppKit  
**Kind**: property

The title of the commands section in the Speech Commands window or `nil` if there is no title.

**Availability**:
- macOS ?+

## Declaration

```swift
var displayedCommandsTitle: String? { get set }
```

#### Discussion

When this property is a non-empty string, commands are displayed in the Speech Commands window indented under a section with this title. If `title` is `nil` or an empty string, the commands are displayed at the top level of the Speech Commands window. This default is not to display the commands under a section title.

## See Also

- [var commands: [String]?](nsspeechrecognizer/commands.md)
  An array of strings defining the commands for which the speech recognizer object should listen.
- [var listensInForegroundOnly: Bool](nsspeechrecognizer/listensinforegroundonly.md)
  A Boolean value that indicates whether the speech recognizer object should only enable its commands when its application is the frontmost one.
- [var blocksOtherRecognizers: Bool](nsspeechrecognizer/blocksotherrecognizers.md)
  A Boolean value that indicates whether the speech recognizer object should block all other recognizers (that is, other applications attempting to understand spoken commands) when listening.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechrecognizer/displayedcommandstitle)*