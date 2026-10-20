# translation(in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

The distance traveled by the mouse during the gesture.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func translation(in view: NSView?) -> NSPoint
```

```objc
- (NSPoint) translationInView:(NSView *) view;
```

#### Return Value

A point whose x and y values correspond to the total distance travelled since the beginning of the gesture.

#### Discussion

The x and y values of the returned point report the total translation over time. They are not delta values from the last time that the translation was reported. To determine the starting point of the gesture, subtract the current translation values from the current location of the mouse in the same view.

## Parameters

- `view`: The view in whose coordinate system the translation of the pan gesture should be computed. The view’s transform is applied to the distance values.

## See Also

### Related Documentation
- [func location(in: NSView?) -> NSPoint](../nsgesturerecognizer/location%28in%29.md)
  Returns the point computed as the location of the gesture.
### Tracking the location and velocity of the gesture
- [func setTranslation(NSPoint, in: NSView?)](./settranslation%28_,in%29.md)
  Changes the current translation value of the gesture recognizer.
- [func velocity(in: NSView?) -> NSPoint](./velocity%28in%29.md)
  The velocity of the pan, measured in points per second.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspangesturerecognizer/translation(in:))*