# createCommandInstance()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Creates and returns an instance of the command object described by the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func createCommandInstance() -> NSScriptCommand
```

```objc
- (NSScriptCommand *) createCommandInstance;
```

## Return Value

The command object, instantiated from [`NSScriptCommand`](../nsscriptcommand.md) or a subclass.

## See Also

### Creating Commands
- [func createCommandInstance(with: NSZone?) -> NSScriptCommand](./createcommandinstance%28with%29.md)
  Creates and returns an instance of the command object described by the receiver in the specified memory zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/createcommandinstance())*