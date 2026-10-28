# setValue(_:forOutputKey:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Sets the value of an output port.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func setValue(_ value: Any!, forOutputKey key: String!) -> Bool
```

```objc
- (BOOL) setValue:(id) value forOutputKey:(NSString *) key;
```

## Return Value

[`true`](../../Swift/true.md) if successful; [`false`](../../Swift/false.md)  if called outside of the [`execute(_:atTime:withArguments:)`](./execute%28_,attime,witharguments%29.md) method.

## Discussion

You call this method from within your [`execute(_:atTime:withArguments:)`](./execute%28_,attime,witharguments%29.md) method to set the output values of your custom patch.

## Parameters

- `value`: The value to associate with the specified key.
- `key`: The key associated with the output port whose value you want to set.

## See Also

### Getting and Setting Port Values
- [func didValue(forInputKeyChange: String!) -> Bool](./didvalue%28forinputkeychange%29.md)
  Returns whether the input port value changed since the last execution of the custom patch.
- [func value(forInputKey: String!) -> Any!](./value%28forinputkey%29.md)
  Returns the current value for an input port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugin/setvalue(_:foroutputkey:))*