# commandName

**Framework**: Foundation  
**Kind**: property

Returns the name of the command.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var commandName: String { get }
```

#### Return Value

The command name as it appears in the application’s scriptability information; may be different from what is displayed to the scripter.

## See Also

- [var appleEventClassCode: FourCharCode](nsscriptcommanddescription/appleeventclasscode.md)
  Returns the four-character code for the Apple event class of the receiver’s command.
- [var appleEventCode: FourCharCode](nsscriptcommanddescription/appleeventcode.md)
  Returns the four-character code for the Apple event ID of the receiver’s command.
- [var commandClassName: String](nsscriptcommanddescription/commandclassname.md)
  Returns the name of the class that will be instantiated to handle the command.
- [var suiteName: String](nsscriptcommanddescription/suitename.md)
  Returns the name of the suite that contains the command described by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/commandname)*