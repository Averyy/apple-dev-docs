# touchBar

**Framework**: AppKit  
**Kind**: property

The [`NSTouchBar`](nstouchbar.md) object associated with the responder.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
var touchBar: NSTouchBar? { get set }
```

#### Discussion

If you have not explicitly provided an [`NSTouchBar`](nstouchbar.md) object for a responder by setting this property, the system sends the [`makeTouchBar()`](nsresponder/maketouchbar().md) message to the responder to create the default bar. This property is archived.

## See Also

- [func makeTouchBar() -> NSTouchBar?](nsresponder/maketouchbar.md)
  Your custom subclass of the `NSResponder` class should override this method to create and configure your subclass’s default [`NSTouchBar`](nstouchbar.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/touchbar)*