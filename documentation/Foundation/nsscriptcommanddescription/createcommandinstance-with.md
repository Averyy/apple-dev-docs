# createCommandInstance(with:)

**Framework**: Foundation  
**Kind**: method

Creates and returns an instance of the command object described by the receiver in the specified memory zone.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func createCommandInstance(with zone: NSZone? = nil) -> NSScriptCommand
```

#### Return Value

The command object, instantiated from [`NSScriptCommand`](nsscriptcommand.md) or a subclass.

## Parameters

- `zone`: The memory zone from which to allocate the command.

## See Also

- [func createCommandInstance() -> NSScriptCommand](nsscriptcommanddescription/createcommandinstance.md)
  Creates and returns an instance of the command object described by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/createcommandinstance(with:))*