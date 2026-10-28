# installsStandardGestureForInteractiveMovement

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the collection view controller installs a standard gesture recognizer to drive the reordering process.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var installsStandardGestureForInteractiveMovement: Bool { get set }
```

```objc
@property (nonatomic) BOOL installsStandardGestureForInteractiveMovement;
```

## Discussion

The default value of this property is [`true`](../../Swift/true.md). When [`true`](../../Swift/true.md), the collection view controller installs a standard gesture recognizer (based on a long-press gesture) to manage the reordering of views inside the collection view. The collection view’s data source must declare its support for reordering items by implementing the appropriate methods. Setting this property to [`false`](../../Swift/false.md) prevents the installation of this gesture recognizer.

## See Also

### Configuring the collection view behavior
- [var clearsSelectionOnViewWillAppear: Bool](./clearsselectiononviewwillappear.md)
  A Boolean value indicating if the controller clears the selection when the collection view appears.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewcontroller/installsstandardgestureforinteractivemovement)*