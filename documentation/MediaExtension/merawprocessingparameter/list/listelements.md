# listElements

**Framework**: MediaExtension  
**Kind**: property  
**Role**: Instance Property

The ordered array of `MERAWProcessingListElementParameter` which make up this list.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var listElements: [MERAWProcessingParameter.ListElement] { get }
```

```objc
@property (readonly) NSArray<MERAWProcessingListElementParameter *> * listElements;
```

## See Also

### Properties
- [var currentValue: Int](./currentvalue.md)
  Get or set the current value for this parameter.
- [var initialValue: Int](./initialvalue.md)
  The initial value for this parameter as defined in the sequence metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessingparameter/list/listelements)*