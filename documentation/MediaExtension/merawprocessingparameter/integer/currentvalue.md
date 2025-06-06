# currentValue

**Framework**: MediaExtension  
**Kind**: property

Get or set the current value for this parameter.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var currentValue: Int { get set }
```

#### Discussion

This property can be observed if appropriate in order to monitor changes to the set of `MERAWProcessingParameters` vended by the extension.

## See Also

- [var initialValue: Int](merawprocessingparameter/integer/initialvalue.md)
  The initial value for this parameter as defined in the sequence metadata.
- [var maximumValue: Int](merawprocessingparameter/integer/maximumvalue.md)
  The maximum value for this parameter.
- [var minimumValue: Int](merawprocessingparameter/integer/minimumvalue.md)
  The minimum value for this parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessingparameter/integer/currentvalue)*