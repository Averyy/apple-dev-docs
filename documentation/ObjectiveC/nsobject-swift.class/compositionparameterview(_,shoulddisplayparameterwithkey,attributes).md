# compositionParameterView(_:shouldDisplayParameterWithKey:attributes:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Allows you to define which composition parameters are visible in the user interface when the composition parameter view refreshes.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func compositionParameterView(_ parameterView: QCCompositionParameterView!, shouldDisplayParameterWithKey portKey: String!, attributes portAttributes: [AnyHashable : Any]! = [:]) -> Bool
```

```objc
- (BOOL) compositionParameterView:(QCCompositionParameterView *) parameterView shouldDisplayParameterWithKey:(NSString *) portKey attributes:(NSDictionary *) portAttributes;
```

## Return Value

Return[`YES`](../yes.md) if the port attributes should be displayed; [`NO`](../no.md) otherwise.

## Parameters

- `parameterView`: The composition parameter view in which the selection changed.
- `portKey`: A key for one of the composition parameters, which is provided to you by the Quartz Composer engine.
- `portAttributes`: A dictionary of the attributes that you want to display in the user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/compositionparameterview(_:shoulddisplayparameterwithkey:attributes:))*