# location(in:)

**Framework**: AppKit  
**Kind**: method

Returns the point computed as the location of the gesture.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func location(in view: NSView?) -> NSPoint
```

#### Return Value

The point at which the gesture occurred. The returned point is in the coordinate system of the specified view, or in the coordinate system of the window if you specified `nil` for the view parameter.

#### Discussion

Use this method to determine the location at which the gesture occurred. Subclasses are responsible for overriding this method and returning an appropriate value based on the type of gesture.

For specific information about what the returned point represents, see the specific gesture recognizer subclass.

## Parameters

- `view`: The view whose coordinate system you want to use for determining the location of the gesture. Specify   to return the point in the coordinate system of the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/location(in:))*