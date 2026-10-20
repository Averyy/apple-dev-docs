# incrementalSearchingShouldDimContentView

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Determines the type of incremental search feedback to be presented

**Availability**:
- macOS 10.7+

## Declaration

```swift
var incrementalSearchingShouldDimContentView: Bool { get set }
```

```objc
@property BOOL incrementalSearchingShouldDimContentView;
```

#### Discussion

If [`true`](../../Swift/true.md), then when an incremental search begins, the `findBarContainer` instance’s parent `contentView` will be dimmed, except for the locations of the incremental matches. If [`false`](../../Swift/false.md), then the incremental matches will not be highlighted automatically, but you can use incrementalMatchRanges to highlight the matches yourself.

The default value is [`true`](../../Swift/true.md).

## See Also

### Incremental Search Configuration
- [class func drawIncrementalMatchHighlight(in: NSRect)](./drawincrementalmatchhighlight%28in%29.md)
  Override this method to draw custom highlighting.
- [var incrementalMatchRanges: [NSValue]](./incrementalmatchranges.md)
  Array of incremental search matches posted on the main queue, which have been found during a background search.
- [var isIncrementalSearchingEnabled: Bool](./isincrementalsearchingenabled.md)
  Determines if incremental searching is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinder/incrementalsearchingshoulddimcontentview)*