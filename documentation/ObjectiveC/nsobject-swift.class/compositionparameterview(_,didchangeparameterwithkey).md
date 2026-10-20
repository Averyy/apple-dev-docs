# compositionParameterView(_:didChangeParameterWithKey:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Called after an input parameter in the composition parameter view has been edited.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func compositionParameterView(_ parameterView: QCCompositionParameterView!, didChangeParameterWithKey portKey: String!)
```

```objc
- (void) compositionParameterView:(QCCompositionParameterView *) parameterView didChangeParameterWithKey:(NSString *) portKey;
```

## Parameters

- `parameterView`: The composition parameter view in which the parameter changed.
- `portKey`: A key for one of the composition parameters, which is provided to you by the Quartz Composer engine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/compositionparameterview(_:didchangeparameterwithkey:))*