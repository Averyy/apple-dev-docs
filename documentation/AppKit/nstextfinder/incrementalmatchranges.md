# incrementalMatchRanges

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Array of incremental search matches posted on the main queue, which have been found during a background search.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var incrementalMatchRanges: [NSValue] { get }
```

```objc
@property (copy, readonly) NSArray<NSValue *> * incrementalMatchRanges;
```

#### Discussion

This array is updated periodically on the main queue as the incremental search operation on a background queue finds matches. You can use this property when incrementalSearchingShouldDimContentView is [`false`](../../Swift/false.md) to know where to draw highlights for incremental matches.

If no incremental search is active, or there are no matches found, this array will be empty. If an incremental search is currently in progress, but not yet complete, this will return all the ranges found so far.

This array is key-value observing compliant and can be observed to know when to update your highlights. When [`new`](../../Foundation/nskeyvalueobservingoptions/new.md) and [`old`](../../Foundation/nskeyvalueobservingoptions/old.md) options are used, the key-value observing change dictionary provides the ranges (and their indexes) that are added or removed. This allows the invalidation of the minimal region necessary to sync highlights with the receiver’s results.

## See Also

### Incremental Search Configuration
- [class func drawIncrementalMatchHighlight(in: NSRect)](./drawincrementalmatchhighlight%28in%29.md)
  Override this method to draw custom highlighting.
- [var isIncrementalSearchingEnabled: Bool](./isincrementalsearchingenabled.md)
  Determines if incremental searching is enabled.
- [var incrementalSearchingShouldDimContentView: Bool](./incrementalsearchingshoulddimcontentview.md)
  Determines the type of incremental search feedback to be presented


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinder/incrementalmatchranges)*