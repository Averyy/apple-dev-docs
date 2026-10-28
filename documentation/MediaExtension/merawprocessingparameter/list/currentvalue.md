# currentValue

**Framework**: MediaExtension  
**Kind**: property  
**Role**: Instance Property

Get or set the current value for this parameter.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var currentValue: Int { get set }
```

```objc
@property (readwrite) NSInteger currentValue;
```

## Discussion

This property can be observed if appropriate in order to monitor changes to the set of `MERAWProcessingParameters` vended by the extension.

## See Also

### Properties
- [var initialValue: Int](./initialvalue.md)
  The initial value for this parameter as defined in the sequence metadata.
- [var listElements: [MERAWProcessingParameter.ListElement]](./listelements.md)
  The ordered array of `MERAWProcessingListElementParameter` which make up this list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessingparameter/list/currentvalue)*