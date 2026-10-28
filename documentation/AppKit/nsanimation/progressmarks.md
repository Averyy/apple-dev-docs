# progressMarks

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array of floating-point numbers representing current progress marks.

**Availability**:
- macOS

## Declaration

```swift
var progressMarks: [NSNumber] { get set }
```

```objc
@property (copy) NSArray<NSNumber *> * progressMarks;
```

## Discussion

The value of this property is an array of [`NSNumber`](../../Foundation/nsnumber.md) objects, each of which contains a float value, which are typed to the [`NSAnimation.Progress`](./progress.md) type. If there are no progress marks, the array is empty. Setting the value of this property is `nil` clears all progress marks.

## See Also

### Managing Progress Marks
- [func addProgressMark(NSAnimation.Progress)](./addprogressmark%28_%29.md)
  Adds the progress mark to the receiver.
- [func removeProgressMark(NSAnimation.Progress)](./removeprogressmark%28_%29.md)
  Removes progress mark from the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimation/progressmarks)*