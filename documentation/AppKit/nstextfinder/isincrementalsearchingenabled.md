# isIncrementalSearchingEnabled

**Framework**: AppKit  
**Kind**: property

Determines if incremental searching is enabled.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var isIncrementalSearchingEnabled: Bool { get set }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/swift/true), then the find bar will do incremental searches. If it returns [`false`](https://developer.apple.com/documentation/swift/false), then the find bar will behave regularly.

The default value is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [class func drawIncrementalMatchHighlight(in: NSRect)](nstextfinder/drawincrementalmatchhighlight(in:).md)
  Override this method to draw custom highlighting.
- [var incrementalMatchRanges: [NSValue]](nstextfinder/incrementalmatchranges.md)
  Array of incremental search matches posted on the main queue, which have been found during a background search.
- [var incrementalSearchingShouldDimContentView: Bool](nstextfinder/incrementalsearchingshoulddimcontentview.md)
  Determines the type of incremental search feedback to be presented


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinder/isincrementalsearchingenabled)*