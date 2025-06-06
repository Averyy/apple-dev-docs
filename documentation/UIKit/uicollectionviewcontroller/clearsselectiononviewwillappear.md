# clearsSelectionOnViewWillAppear

**Framework**: UIKit  
**Kind**: property

A Boolean value indicating if the controller clears the selection when the collection view appears.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var clearsSelectionOnViewWillAppear: Bool { get set }
```

#### Discussion

The default value of this property is [`true`](https://developer.apple.com/documentation/swift/true). When [`true`](https://developer.apple.com/documentation/swift/true), the collection view controller clears the collection view’s current selection when it receives a [`viewWillAppear(_:)`](uiviewcontroller/viewwillappear(_:).md) message. Setting this property to [`false`](https://developer.apple.com/documentation/swift/false) preserves the selection.

## See Also

- [var installsStandardGestureForInteractiveMovement: Bool](uicollectionviewcontroller/installsstandardgestureforinteractivemovement.md)
  A Boolean value indicating whether the collection view controller installs a standard gesture recognizer to drive the reordering process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewcontroller/clearsselectiononviewwillappear)*