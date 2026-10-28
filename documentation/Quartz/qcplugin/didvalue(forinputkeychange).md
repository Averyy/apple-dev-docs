# didValue(forInputKeyChange:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Returns whether the input port value changed since the last execution of the custom patch.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func didValue(forInputKeyChange key: String!) -> Bool
```

```objc
- (BOOL) didValueForInputKeyChange:(NSString *) key;
```

## Return Value

[`true`](../../Swift/true.md) if the value on the input port changed since the last time the [`execute(_:atTime:withArguments:)`](./execute%28_,attime,witharguments%29.md) method was called; always returns [`false`](../../Swift/false.md) if called outside of the `execute:atTime:withArguments:` method.

## Parameters

- `key`: The key for the input port whose value you want to check.

## See Also

### Getting and Setting Port Values
- [func value(forInputKey: String!) -> Any!](./value%28forinputkey%29.md)
  Returns the current value for an input port.
- [func setValue(Any!, forOutputKey: String!) -> Bool](./setvalue%28_,foroutputkey%29.md)
  Sets the value of an output port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugin/didvalue(forinputkeychange:))*