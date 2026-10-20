# currentValue

**Framework**: MediaExtension  
**Kind**: property  
**Role**: Instance Property

Get or set the current value for this parameter.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var currentValue: Float { get set }
```

```objc
@property (readwrite) float currentValue;
```

#### Discussion

This property can be observed if appropriate in order to monitor changes to the set of `MERAWProcessingParameters` vended by the extension.

## See Also

### Properties
- [var initialValue: Float](./initialvalue.md)
  The initial value for this parameter as defined in the sequence metadata.
- [var maximumValue: Float](./maximumvalue.md)
  The maximum value for this parameter.
- [var minimumValue: Float](./minimumvalue.md)
  The minimum value for this parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessingparameter/floatingpoint/currentvalue)*