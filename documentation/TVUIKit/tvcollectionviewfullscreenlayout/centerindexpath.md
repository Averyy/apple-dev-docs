# centerIndexPath

**Framework**: TVUIKit  
**Kind**: property  
**Role**: Instance Property

The index path of the currently centered item.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
var centerIndexPath: IndexPath? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) NSIndexPath * centerIndexPath;
```

## Discussion

The `centerIndexPath` property returns the index path of the cell currently centered on the screen. `TVUIKit` calculates the current index path using the current content offset of the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvcollectionviewfullscreenlayout/centerindexpath)*