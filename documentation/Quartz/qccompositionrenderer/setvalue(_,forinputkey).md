# setValue(_:forInputKey:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sets the value for an input port of a composition.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func setValue(_ value: Any!, forInputKey key: String!) -> Bool
```

```objc
- (BOOL) setValue:(id) value forInputKey:(NSString *) key;
```

## Return Value

Returns [`false`](../../Swift/false.md) if it cannot set the value.

## Parameters

- `value`: The value to set for the input port. The input port must be at the root patch of the composition. The data type of the `value` argument must match the input port. See [`QCPortAttributeTypeKey`](../qcportattributetypekey.md) for the data types accepted by a particular port type.
- `key`: The key associated with the input port of the composition. This method throws an exception if `key` is invalid.

## See Also

### Passing and Retrieving Values From a Composition
- [func value(forInputKey: String!) -> Any!](./value%28forinputkey%29.md)
  Returns the value for an input port of a composition.
- [func value(forOutputKey: String!) -> Any!](./value%28foroutputkey%29.md)
  Returns the value for an output port of a composition.
- [func value(forOutputKey: String!, ofType: String!) -> Any!](./value%28foroutputkey,oftype%29.md)
  Returns the current value on an output port (identified by its key) of the root patch of the composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionrenderer/setvalue(_:forinputkey:))*