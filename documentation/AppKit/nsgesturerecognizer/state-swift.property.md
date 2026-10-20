# state

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The current state of the gesture recognizer.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var state: NSGestureRecognizer.State { get set }
```

```objc
@property (readonly) NSGestureRecognizerState state;
```

#### Discussion

This property conveys where the gesture recognizer is in the recognition process. The default declaration of this property is read-only so that external clients (such as other gesture recognizers) can use the value for informational purposes. Subclasses can redeclare the property as read-write internally. When doing so, you do not need to provide a custom implementation to set the value of the property. This class provides an implementation that detects state transitions and updates the gesture recognizer accordingly.

For more information about the state transitions that can occur in a gesture recognizer, see [State Transitions](../nsgesturerecognizer.md#State-Transitions).

## See Also

### Accessing the recognizer’s state
- [var view: NSView?](./view.md)
  The view to which the gesture recognizer is attached.
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value indicating whether the gesture recognizer is able to handle events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/state-swift.property)*