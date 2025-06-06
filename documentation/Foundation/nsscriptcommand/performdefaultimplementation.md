# performDefaultImplementation()

**Framework**: Foundation  
**Kind**: method

Overridden by subclasses to provide a default implementation for the command represented by the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func performDefaultImplementation() -> Any?
```

#### Discussion

Do not invoke this method directly. [`execute()`](nsscriptcommand/execute().md) invokes this method when the command being executed is not supported by the class of the objects receiving the command. The default implementation returns `nil`.

You need to create a subclass of `NSScriptCommand` only if you need to provide a default implementation of a command.

## See Also

- [func execute() -> Any?](nsscriptcommand/execute.md)
  Executes the command if it is valid and returns the result, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptcommand/performdefaultimplementation())*