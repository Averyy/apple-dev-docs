# value(forOutputKey:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the value for an output port of a composition.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func value(forOutputKey key: String!) -> Any!
```

```objc
- (id) valueForOutputKey:(NSString *) key;
```

#### Return Value

The value. The data type of returned value depends on the type of the output port. See [`QCPortAttributeTypeKey`](../qcportattributetypekey.md) for more information.

## Parameters

- `key`: The key associated with an output port for the root patch of a composition. This method throws an exception if `key` is invalid.

## See Also

### Passing and Retrieving Values From a Composition
- [func setValue(Any!, forInputKey: String!) -> Bool](./setvalue%28_,forinputkey%29.md)
  Sets the value for an input port of a composition.
- [func value(forInputKey: String!) -> Any!](./value%28forinputkey%29.md)
  Returns the value for an input port of a composition.
- [func value(forOutputKey: String!, ofType: String!) -> Any!](./value%28foroutputkey,oftype%29.md)
  Returns the current value on an output port (identified by its key) of the root patch of the composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionrenderer/value(foroutputkey:))*