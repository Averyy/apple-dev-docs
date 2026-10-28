# touchBar

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The [`NSTouchBar`](../nstouchbar.md) object associated with the responder.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
var touchBar: NSTouchBar? { get set }
```

```objc
@property (strong, readwrite, nullable) NSTouchBar * touchBar;
```

## Discussion

If you have not explicitly provided an [`NSTouchBar`](../nstouchbar.md) object for a responder by setting this property, the system sends the [`makeTouchBar()`](./maketouchbar%28%29.md) message to the responder to create the default bar. This property is archived.

## See Also

### Supporting the Touch Bar
- [func makeTouchBar() -> NSTouchBar?](./maketouchbar%28%29.md)
  Your custom subclass of the `NSResponder` class should override this method to create and configure your subclass’s default [`NSTouchBar`](../nstouchbar.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/touchbar)*