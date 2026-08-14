# drawIncrementalMatchHighlight(in:)

**Framework**: AppKit  
**Kind**: method

Override this method to draw custom highlighting.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class func drawIncrementalMatchHighlight(in rect: NSRect)
```

#### Discussion

If [`incrementalSearchingShouldDimContentView`](nstextfinder/incrementalsearchingshoulddimcontentview.md) is [`false`](https://developer.apple.com/documentation/swift/false), it is recommended to highlight incremental matches in your own view. However, some applications may choose to show incremental search values in a different manner.

This method is not recommended to be overridden. The text finder never calls it. The view calls it to get the standard highlight behavior. It is recommended that views use this method do draw the highlight for consistency and to allow Application Kit to tweak the behavior in the future. If the view wants custom drawing, then it should be implemented by the view.

The common usage pattern for this is: draw the background,  draw the incremental match highlights for the [`incrementalMatchRanges`](nstextfinder/incrementalmatchranges.md), and then draw the text.

## Parameters

- `rect`: The rectangle that needs to be drawn highlighted in the current coordinate system.

## See Also

- [var incrementalMatchRanges: [NSValue]](nstextfinder/incrementalmatchranges.md)
  Array of incremental search matches posted on the main queue, which have been found during a background search.
- [var isIncrementalSearchingEnabled: Bool](nstextfinder/isincrementalsearchingenabled.md)
  Determines if incremental searching is enabled.
- [var incrementalSearchingShouldDimContentView: Bool](nstextfinder/incrementalsearchingshoulddimcontentview.md)
  Determines the type of incremental search feedback to be presented


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinder/drawincrementalmatchhighlight(in:))*