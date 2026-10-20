# touchState

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

The state of the user’s touch on the surface of the touchpad.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var touchState: GCControllerTouchpad.TouchState { get }
```

```objc
@property (nonatomic, readonly) GCTouchState touchState;
```

## See Also

### Accessing the input values
- [GCControllerTouchpad.TouchState](./touchstate-swift.enum.md)
  The possible states of the user’s touch.
- [var reportsAbsoluteTouchSurfaceValues: Bool](./reportsabsolutetouchsurfacevalues.md)
  A Boolean value that determines whether the touch values are absolute or relative.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollertouchpad/touchstate-swift.property)*