# selectedIndex

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The currently selected index.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
var selectedIndex: Int { get set }
```

```objc
@property (nonatomic, assign) NSInteger selectedIndex;
```

## Discussion

The default value is `0`. You can only set a value that’s greater than or equal to `0` and less than [`numberOfIndexes`](./numberofindexes.md).

> ❗ **Important**:  Only modify the selected index from the same dispatch queue that you specified in the control’s [`setActionQueue:action:`](../avcaptureslider/setactionqueue_action_.md) method.

## See Also

### Accessing the control value
- [var numberOfIndexes: Int](./numberofindexes.md)
  The number of index values the control provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureindexpicker/selectedindex)*