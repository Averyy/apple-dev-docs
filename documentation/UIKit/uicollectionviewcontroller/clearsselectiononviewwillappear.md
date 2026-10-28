# clearsSelectionOnViewWillAppear

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating if the controller clears the selection when the collection view appears.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var clearsSelectionOnViewWillAppear: Bool { get set }
```

```objc
@property (nonatomic) BOOL clearsSelectionOnViewWillAppear;
```

## Discussion

The default value of this property is [`true`](../../Swift/true.md). When [`true`](../../Swift/true.md), the collection view controller clears the collection view’s current selection when it receives a [`viewWillAppear(_:)`](../uiviewcontroller/viewwillappear%28_%29.md) message. Setting this property to [`false`](../../Swift/false.md) preserves the selection.

## See Also

### Configuring the collection view behavior
- [var installsStandardGestureForInteractiveMovement: Bool](./installsstandardgestureforinteractivemovement.md)
  A Boolean value indicating whether the collection view controller installs a standard gesture recognizer to drive the reordering process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewcontroller/clearsselectiononviewwillappear)*