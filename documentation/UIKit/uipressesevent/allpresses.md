# allPresses

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The state of all physical buttons in the event.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var allPresses: Set<UIPress> { get }
```

```objc
@property (nonatomic, readonly) NSSet<UIPress *> * allPresses;
```

## Return Value

The set of [`UIPress`](../uipress.md) instances that participated in this event.

## See Also

### Reading the event button presses
- [func presses(for: UIGestureRecognizer) -> Set<UIPress>](./presses%28for%29.md)
  Returns the state of all physical buttons in the event that are associated with a particular gesture recognizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipressesevent/allpresses)*