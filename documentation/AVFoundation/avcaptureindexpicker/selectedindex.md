# selectedIndex

**Framework**: AVFoundation  
**Kind**: property

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

#### Discussion

The default value is `0`. You can only set a value that’s greater than or equal to `0` and less than [`numberOfIndexes`](avcaptureindexpicker/numberofindexes.md).

> ❗ **Important**:  Only modify the selected index from the same dispatch queue that you specified in the control’s [`setActionQueue:action:`](avcaptureslider/setactionqueue:action:.md) method.

 Only modify the selected index from the same dispatch queue that you specified in the control’s [`setActionQueue:action:`](avcaptureslider/setactionqueue:action:.md) method.

## See Also

- [var numberOfIndexes: Int](avcaptureindexpicker/numberofindexes.md)
  The number of index values the control provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureindexpicker/selectedindex)*