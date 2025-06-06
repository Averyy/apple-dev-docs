# suiteName

**Framework**: Foundation  
**Kind**: property

Returns the name of the suite that contains the command described by the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var suiteName: String { get }
```

#### Return Value

The receiver’s suite name. Within an application’s scriptability information, named suites contain related sets of information.

## See Also

- [var appleEventClassCode: FourCharCode](nsscriptcommanddescription/appleeventclasscode.md)
  Returns the four-character code for the Apple event class of the receiver’s command.
- [var appleEventCode: FourCharCode](nsscriptcommanddescription/appleeventcode.md)
  Returns the four-character code for the Apple event ID of the receiver’s command.
- [var commandClassName: String](nsscriptcommanddescription/commandclassname.md)
  Returns the name of the class that will be instantiated to handle the command.
- [var commandName: String](nsscriptcommanddescription/commandname.md)
  Returns the name of the command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/suitename)*