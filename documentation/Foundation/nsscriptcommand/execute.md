# execute()

**Framework**: Foundation  
**Kind**: method

Executes the command if it is valid and returns the result, if any.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func execute() -> Any?
```

#### Discussion

Before this method executes the command (through `NSInvocation` mechanisms), it evaluates all object specifiers involved in the command, validates that the receivers can actually handle the command, and verifies that the types of any arguments that were initially object specifiers are valid.

You shouldn’t have to override this method. If the command’s receivers want to handle the command themselves, this method invokes their defined handler. Otherwise, it invokes [`performDefaultImplementation()`](nsscriptcommand/performdefaultimplementation().md).

## See Also

- [var evaluatedReceivers: Any?](nsscriptcommand/evaluatedreceivers.md)
  Returns the object or objects to which the command is to be sent (called both the “receivers” or “targets” of script commands).
- [var evaluatedArguments: [String : Any]?](nsscriptcommand/evaluatedarguments.md)
  Returns a dictionary containing the arguments of the command, evaluated from object specifiers to objects if necessary. The keys in the dictionary are the argument names.
- [func performDefaultImplementation() -> Any?](nsscriptcommand/performdefaultimplementation.md)
  Overridden by subclasses to provide a default implementation for the command represented by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptcommand/execute())*