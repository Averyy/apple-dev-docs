# setValue(_:forInputKey:)

**Framework**: Quartz  
**Kind**: method  
**Required**: Yes

Sets the value for an input port of a composition.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func setValue(_ value: Any!, forInputKey key: String!) -> Bool
```

#### Return Value

Returns [`false`](https://developer.apple.com/documentation/Swift/false) if it cannot set the value.

## Parameters

- `value`: The value to set for the input port. The input port must be at the root patch of the composition. The data type of the   argument must match the input port. See   for the data types accepted by a particular port type.
- `key`: The key associated with the input port of the composition. This method throws an exception if   is invalid.

## See Also

- [func value(forInputKey: String!) -> Any!](qccompositionrenderer/value(forinputkey:).md)
  Returns the value for an input port of a composition.
- [func value(forOutputKey: String!) -> Any!](qccompositionrenderer/value(foroutputkey:).md)
  Returns the value for an output port of a composition.
- [func value(forOutputKey: String!, ofType: String!) -> Any!](qccompositionrenderer/value(foroutputkey:oftype:).md)
  Returns the current value on an output port (identified by its key) of the root patch of the composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionrenderer/setvalue(_:forinputkey:))*