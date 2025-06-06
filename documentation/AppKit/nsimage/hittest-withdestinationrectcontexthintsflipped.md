# hitTest(_:withDestinationRect:context:hints:flipped:)

**Framework**: AppKit  
**Kind**: method

Returns whether the destination rectangle would intersect a non-transparent portion of the image.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func hitTest(_ testRectDestSpace: NSRect, withDestinationRect imageRectDestSpace: NSRect, context: NSGraphicsContext?, hints: [NSImageRep.HintKey : Any]?, flipped: Bool) -> Bool
```

#### Return Value

YES if the `testRectDestSpace` intersects with non-transparent content within the `imageRectDestSpace`, otherwise NO.

#### Discussion

This method simulates the results of hit-testing the test rectangle as if the image was drawn in the graphics context using the provided hints and respecting the specified flippedness.

## Parameters

- `testRectDestSpace`: The rectangle to hit test.
- `imageRectDestSpace`: A rectangle representing the drawn size of the image.
- `context`: A graphics context. This value can be  .
- `hints`: An optional dictionary of hints that provide more context for selecting or generating a  , and may override properties of the  . See   for a summary of the possible key-value pairs.
- `flipped`:   if the image is flipped, otherwise  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/hittest(_:withdestinationrect:context:hints:flipped:))*