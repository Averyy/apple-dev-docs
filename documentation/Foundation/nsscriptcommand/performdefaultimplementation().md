# performDefaultImplementation()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Overridden by subclasses to provide a default implementation for the command represented by the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func performDefaultImplementation() -> Any?
```

```objc
- (id) performDefaultImplementation;
```

## Discussion

Do not invoke this method directly. [`execute()`](./execute%28%29.md) invokes this method when the command being executed is not supported by the class of the objects receiving the command. The default implementation returns `nil`.

You need to create a subclass of `NSScriptCommand` only if you need to provide a default implementation of a command.

## See Also

### Executing the command
- [func execute() -> Any?](./execute%28%29.md)
  Executes the command if it is valid and returns the result, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptcommand/performdefaultimplementation())*