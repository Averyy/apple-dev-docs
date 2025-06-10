# showsCloseControl

**Framework**: MapKit JS  
**Kind**: property

A Boolean value that indicates whether the Look Around view displays a close control.

**Availability**:
- MapKit JS 5.79+

## Declaration

```swift
attribute boolean showsCloseControl;
```

#### Discussion

When the user interacts with the close control, a `close` event dispatches. To handle the `close` event, cancel the event and invoke appropriate actions for your application to close the view. If the event is not cancelled, Look Around view will remove itself from the DOM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/lookaroundoptions/showsclosecontrol)*