# rect(for:)

**Framework**: AppKit  
**Kind**: method

Returns the rectangle occupied by `aPart`, which for this method is interpreted literally rather than as an indicator of scrolling direction.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func rect(for partCode: NSScroller.Part) -> NSRect
```

#### Discussion

See [`NSScroller.Part`](nsscroller/part.md) for a list of possible values for `aPart`.

Note the interpretations of `NSScrollerDecrementPage` and `NSScrollerIncrementPage`. The actual part of an NSScroller that causes page-by-page scrolling varies, so as a convenience these part codes refer to useful parts different from the scroll buttons.

Returns `NSZeroRect` if the part requested isn’t present on the receiver.

## See Also

- [var hitPart: NSScroller.Part](nsscroller/hitpart.md)
  A part code indicating the manner in which the scrolling should be performed.
- [func testPart(NSPoint) -> NSScroller.Part](nsscroller/testpart(_:).md)
  Returns the part that would be hit by a mouse-down event at `aPoint` (expressed in the window’s coordinate system).
- [func checkSpaceForParts()](nsscroller/checkspaceforparts.md)
  Checks to see if there is enough room in the receiver to display the knob and buttons.
- [var usableParts: NSScroller.UsableParts](nsscroller/usableparts-swift.property.md)
  A value that indicates which parts of the receiver are displayed and usable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscroller/rect(for:))*