# incrementalSearchingShouldDimContentView

**Framework**: AppKit  
**Kind**: property

Determines the type of incremental search feedback to be presented

**Availability**:
- macOS 10.7+

## Declaration

```swift
var incrementalSearchingShouldDimContentView: Bool { get set }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/swift/true), then when an incremental search begins, the `findBarContainer` instance’s parent `contentView` will be dimmed, except for the locations of the incremental matches. If [`false`](https://developer.apple.com/documentation/swift/false), then the incremental matches will not be highlighted automatically, but you can use incrementalMatchRanges to highlight the matches yourself.

The default value is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [class func drawIncrementalMatchHighlight(in: NSRect)](nstextfinder/drawincrementalmatchhighlight(in:).md)
  Override this method to draw custom highlighting.
- [var incrementalMatchRanges: [NSValue]](nstextfinder/incrementalmatchranges.md)
  Array of incremental search matches posted on the main queue, which have been found during a background search.
- [var isIncrementalSearchingEnabled: Bool](nstextfinder/isincrementalsearchingenabled.md)
  Determines if incremental searching is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinder/incrementalsearchingshoulddimcontentview)*