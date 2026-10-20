# view

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The view to which the gesture recognizer is attached.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var view: NSView? { get }
```

```objc
@property (readonly, nullable) NSView * view;
```

#### Discussion

To attach a gesture recognizer to a view, call the [`addGestureRecognizer(_:)`](../nsview/addgesturerecognizer%28_%29.md) method of the view. If the gesture recognizer is not attached to a view, the value in this property is `nil`.

## See Also

### Related Documentation
- [func location(in: NSView?) -> NSPoint](./location%28in%29.md)
  Returns the point computed as the location of the gesture.
### Accessing the recognizer’s state
- [var state: NSGestureRecognizer.State](./state-swift.property.md)
  The current state of the gesture recognizer.
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value indicating whether the gesture recognizer is able to handle events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/view)*