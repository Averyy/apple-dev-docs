# setDefaultValue(_:forInputKey:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Sets the default value to use for a composition input parameter.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func setDefaultValue(_ value: Any!, forInputKey key: String!)
```

```objc
- (void) setDefaultValue:(id) value forInputKey:(NSString *) key;
```

## Parameters

- `value`: This default value overrides any initial value existing for composition input parameters with this key. Pass `nil` to clear the default value.
- `key`: The input parameter key whose default value you want to set.

## See Also

### Setting Composition Input Parameters
- [func resetDefaultInputValues()](./resetdefaultinputvalues%28%29.md)
  Clears all previously set default values for composition input parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionpickerview/setdefaultvalue(_:forinputkey:))*