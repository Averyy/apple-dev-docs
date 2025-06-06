# translation(in:)

**Framework**: AppKit  
**Kind**: method

The distance traveled by the mouse during the gesture.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func translation(in view: NSView?) -> NSPoint
```

#### Return Value

A point whose x and y values correspond to the total distance travelled since the beginning of the gesture.

#### Discussion

The x and y values of the returned point report the total translation over time. They are not delta values from the last time that the translation was reported. To determine the starting point of the gesture, subtract the current translation values from the current location of the mouse in the same view.

## Parameters

- `view`: The view in whose coordinate system the translation of the pan gesture should be computed. The view’s transform is applied to the distance values.

## See Also

- [func location(in: NSView?) -> NSPoint](nsgesturerecognizer/location(in:).md)
  Returns the point computed as the location of the gesture.
- [func setTranslation(NSPoint, in: NSView?)](nspangesturerecognizer/settranslation(_:in:).md)
  Changes the current translation value of the gesture recognizer.
- [func velocity(in: NSView?) -> NSPoint](nspangesturerecognizer/velocity(in:).md)
  The velocity of the pan, measured in points per second.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspangesturerecognizer/translation(in:))*