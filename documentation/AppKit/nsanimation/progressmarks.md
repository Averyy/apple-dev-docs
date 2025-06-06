# progressMarks

**Framework**: AppKit  
**Kind**: property

An array of floating-point numbers representing current progress marks.

**Availability**:
- macOS ?+

## Declaration

```swift
var progressMarks: [NSNumber] { get set }
```

#### Discussion

The value of this property is an array of [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) objects, each of which contains a float value, which are typed to the [`NSAnimation.Progress`](nsanimation/progress.md) type. If there are no progress marks, the array is empty. Setting the value of this property is `nil` clears all progress marks.

## See Also

- [func addProgressMark(NSAnimation.Progress)](nsanimation/addprogressmark(_:).md)
  Adds the progress mark to the receiver.
- [func removeProgressMark(NSAnimation.Progress)](nsanimation/removeprogressmark(_:).md)
  Removes progress mark from the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimation/progressmarks)*