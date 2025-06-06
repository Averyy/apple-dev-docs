# value(forInputKey:)

**Framework**: Quartz  
**Kind**: method

Returns the current value for an input port.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func value(forInputKey key: String!) -> Any!
```

#### Return Value

The value associated with the key or `nil` if called outside of the [`execute(_:atTime:withArguments:)`](qcplugin/execute(_:attime:witharguments:).md) method.

#### Discussion

You call this method from within your [`execute(_:atTime:withArguments:)`](qcplugin/execute(_:attime:witharguments:).md) method to retrieve the input values of your custom patch.

## Parameters

- `key`: The key for the input port you want to check.

## See Also

- [func didValue(forInputKeyChange: String!) -> Bool](qcplugin/didvalue(forinputkeychange:).md)
  Returns whether the input port value changed since the last execution of the custom patch.
- [func setValue(Any!, forOutputKey: String!) -> Bool](qcplugin/setvalue(_:foroutputkey:).md)
  Sets the value of an output port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugin/value(forinputkey:))*