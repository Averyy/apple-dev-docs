# appleEventClassCode

**Framework**: Foundation  
**Kind**: property

Returns the four-character code for the Apple event class of the receiver’s command.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var appleEventClassCode: FourCharCode { get }
```

#### Return Value

The Apple event code associated with the receiver’s command. This is the primary code used to identify the command in Apple events.

#### Discussion

In an Apple event that specifies a script command, two four character codes—the event class and event ID—together identify the command. You use this method to obtain the event class. You use [`appleEventCode`](nsscriptcommanddescription/appleeventcode.md) to obtain the event ID.

For example, commands in AppleScript’s Core suite, such as `clone`, `count`, and `create`, have an event class code of `'core'`. This code and the event ID code returned by `appleEventCode` together specify the necessary information for identifying and dispatching an Apple event.

## See Also

- [var appleEventCode: FourCharCode](nsscriptcommanddescription/appleeventcode.md)
  Returns the four-character code for the Apple event ID of the receiver’s command.
- [var commandClassName: String](nsscriptcommanddescription/commandclassname.md)
  Returns the name of the class that will be instantiated to handle the command.
- [var commandName: String](nsscriptcommanddescription/commandname.md)
  Returns the name of the command.
- [var suiteName: String](nsscriptcommanddescription/suitename.md)
  Returns the name of the suite that contains the command described by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/appleeventclasscode)*