# title

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The title string associated with the point of interest.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- macOS 10.11.4+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var title: String { get }
```

```objc
@property (nonatomic, strong, readonly) NSString * title;
```

#### Discussion

The local search completion object ensures this string isn’t empty.

## See Also

### Getting the search completions
- [var subtitle: String](./subtitle.md)
  The subtitle (if any) associated with the point of interest.
- [var titleHighlightRanges: [NSValue]](./titlehighlightranges.md)
  The ranges of characters to highlight in the title string.
- [var subtitleHighlightRanges: [NSValue]](./subtitlehighlightranges.md)
  The ranges of characters to highlight in the subtitle string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalsearchcompletion/title)*