# setValue(_:forOutputKey:)

**Framework**: Quartz  
**Kind**: method

Sets the value of an output port.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func setValue(_ value: Any!, forOutputKey key: String!) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if successful; [`false`](https://developer.apple.com/documentation/Swift/false)  if called outside of the [`execute(_:atTime:withArguments:)`](qcplugin/execute(_:attime:witharguments:).md) method.

#### Discussion

You call this method from within your [`execute(_:atTime:withArguments:)`](qcplugin/execute(_:attime:witharguments:).md) method to set the output values of your custom patch.

## Parameters

- `value`: The value to associate with the specified key.
- `key`: The key associated with the output port whose value you want to set.

## See Also

- [func didValue(forInputKeyChange: String!) -> Bool](qcplugin/didvalue(forinputkeychange:).md)
  Returns whether the input port value changed since the last execution of the custom patch.
- [func value(forInputKey: String!) -> Any!](qcplugin/value(forinputkey:).md)
  Returns the current value for an input port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugin/setvalue(_:foroutputkey:))*