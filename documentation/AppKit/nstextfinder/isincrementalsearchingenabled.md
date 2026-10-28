# isIncrementalSearchingEnabled

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Determines if incremental searching is enabled.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var isIncrementalSearchingEnabled: Bool { get set }
```

```objc
@property (getter=isIncrementalSearchingEnabled) BOOL incrementalSearchingEnabled;
```

## Discussion

If [`true`](../../Swift/true.md), then the find bar will do incremental searches. If it returns [`false`](../../Swift/false.md), then the find bar will behave regularly.

The default value is [`false`](../../Swift/false.md).

## See Also

### Incremental Search Configuration
- [class func drawIncrementalMatchHighlight(in: NSRect)](./drawincrementalmatchhighlight%28in%29.md)
  Override this method to draw custom highlighting.
- [var incrementalMatchRanges: [NSValue]](./incrementalmatchranges.md)
  Array of incremental search matches posted on the main queue, which have been found during a background search.
- [var incrementalSearchingShouldDimContentView: Bool](./incrementalsearchingshoulddimcontentview.md)
  Determines the type of incremental search feedback to be presented


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinder/isincrementalsearchingenabled)*