# value(forInputKey:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Returns the current value for an input port.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func value(forInputKey key: String!) -> Any!
```

```objc
- (id) valueForInputKey:(NSString *) key;
```

## Return Value

The value associated with the key or `nil` if called outside of the [`execute(_:atTime:withArguments:)`](./execute%28_,attime,witharguments%29.md) method.

## Discussion

You call this method from within your [`execute(_:atTime:withArguments:)`](./execute%28_,attime,witharguments%29.md) method to retrieve the input values of your custom patch.

## Parameters

- `key`: The key for the input port you want to check.

## See Also

### Getting and Setting Port Values
- [func didValue(forInputKeyChange: String!) -> Bool](./didvalue%28forinputkeychange%29.md)
  Returns whether the input port value changed since the last execution of the custom patch.
- [func setValue(Any!, forOutputKey: String!) -> Bool](./setvalue%28_,foroutputkey%29.md)
  Sets the value of an output port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugin/value(forinputkey:))*