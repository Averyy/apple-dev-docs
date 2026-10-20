# testPart(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the part that would be hit by a mouse-down event at `aPoint` (expressed in the window’s coordinate system).

**Availability**:
- macOS

## Declaration

```swift
func testPart(_ point: NSPoint) -> NSScroller.Part
```

```objc
- (NSScrollerPart) testPart:(NSPoint) point;
```

#### Discussion

See [`NSScroller.Part`](./part.md) for a list of possible return values. In macOS 10.7 and later, this method no longer returns [`NSScroller.Part.incrementLine`](./part/incrementline.md) or [`NSScroller.Part.decrementLine`](./part/decrementline.md).

Note the interpretations of `NSScrollerDecrementPage` and `NSScrollerIncrementPage`. The actual part of a scroller that causes page-by-page scrolling varies, so as a convenience these part codes refer to useful parts different from the scroll buttons.

## See Also

### Related Documentation
- [var hitPart: NSScroller.Part](./hitpart.md)
  A part code indicating the manner in which the scrolling should be performed.
### Calculating Layout
- [func rect(for: NSScroller.Part) -> NSRect](./rect%28for%29.md)
  Returns the rectangle occupied by `aPart`, which for this method is interpreted literally rather than as an indicator of scrolling direction.
- [func checkSpaceForParts()](./checkspaceforparts%28%29.md)
  Checks to see if there is enough room in the receiver to display the knob and buttons.
- [var usableParts: NSScroller.UsableParts](./usableparts-swift.property.md)
  A value that indicates which parts of the receiver are displayed and usable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscroller/testpart(_:))*