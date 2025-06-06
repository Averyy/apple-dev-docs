# value(forInputKey:)

**Framework**: Quartz  
**Kind**: method  
**Required**: Yes

Returns the value for an input port of a composition.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func value(forInputKey key: String!) -> Any!
```

#### Return Value

The value. The data type of returned value depends on the type of the input port. See [`QCPortAttributeTypeKey`](qcportattributetypekey.md) for more information.

## Parameters

- `key`: The key associated with an input port for the root patch of a composition. This method throws an exception if   is invalid.

## See Also

- [func setValue(Any!, forInputKey: String!) -> Bool](qccompositionrenderer/setvalue(_:forinputkey:).md)
  Sets the value for an input port of a composition.
- [func value(forOutputKey: String!) -> Any!](qccompositionrenderer/value(foroutputkey:).md)
  Returns the value for an output port of a composition.
- [func value(forOutputKey: String!, ofType: String!) -> Any!](qccompositionrenderer/value(foroutputkey:oftype:).md)
  Returns the current value on an output port (identified by its key) of the root patch of the composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionrenderer/value(forinputkey:))*