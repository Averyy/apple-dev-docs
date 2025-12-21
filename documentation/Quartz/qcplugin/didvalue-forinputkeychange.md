# didValue(forInputKeyChange:)

**Framework**: Quartz  
**Kind**: method

Returns whether the input port value changed since the last execution of the custom patch.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func didValue(forInputKeyChange key: String!) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the value on the input port changed since the last time the [`execute(_:atTime:withArguments:)`](qcplugin/execute(_:attime:witharguments:).md) method was called; always returns [`false`](https://developer.apple.com/documentation/Swift/false) if called outside of the `execute:atTime:withArguments:` method.

## Parameters

- `key`: The key for the input port whose value you want to check.

## See Also

- [func value(forInputKey: String!) -> Any!](qcplugin/value(forinputkey:).md)
  Returns the current value for an input port.
- [func setValue(Any!, forOutputKey: String!) -> Bool](qcplugin/setvalue(_:foroutputkey:).md)
  Sets the value of an output port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugin/didvalue(forinputkeychange:))*