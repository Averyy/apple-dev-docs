# resetDefaultInputValues()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Clears all previously set default values for composition input parameters.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func resetDefaultInputValues()
```

```objc
- (void) resetDefaultInputValues;
```

## Discussion

This method resets the defaults that were set with the method [`setDefaultValue(_:forInputKey:)`](./setdefaultvalue%28_,forinputkey%29.md).

## See Also

### Setting Composition Input Parameters
- [func setDefaultValue(Any!, forInputKey: String!)](./setdefaultvalue%28_,forinputkey%29.md)
  Sets the default value to use for a composition input parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionpickerview/resetdefaultinputvalues())*