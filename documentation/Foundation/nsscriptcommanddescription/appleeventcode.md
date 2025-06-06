# appleEventCode

**Framework**: Foundation  
**Kind**: property

Returns the four-character code for the Apple event ID of the receiver’s command.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var appleEventCode: FourCharCode { get }
```

#### Return Value

The code for the event ID of the receiver’s command.

#### Discussion

This value of the event ID returned by this method, together with the event class code returned by [`appleEventClassCode`](nsscriptcommanddescription/appleeventclasscode.md), specifies the necessary information for identifying and dispatching an Apple event.

## See Also

- [var appleEventCodeForReturnType: FourCharCode](nsscriptcommanddescription/appleeventcodeforreturntype.md)
  Returns the Apple event code that identifies the command’s return type.
- [func appleEventCodeForArgument(withName: String) -> FourCharCode](nsscriptcommanddescription/appleeventcodeforargument(withname:).md)
  Returns the Apple event code for the specified command argument of the receiver.
- [var appleEventClassCode: FourCharCode](nsscriptcommanddescription/appleeventclasscode.md)
  Returns the four-character code for the Apple event class of the receiver’s command.
- [var commandClassName: String](nsscriptcommanddescription/commandclassname.md)
  Returns the name of the class that will be instantiated to handle the command.
- [var commandName: String](nsscriptcommanddescription/commandname.md)
  Returns the name of the command.
- [var suiteName: String](nsscriptcommanddescription/suitename.md)
  Returns the name of the suite that contains the command described by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/appleeventcode)*