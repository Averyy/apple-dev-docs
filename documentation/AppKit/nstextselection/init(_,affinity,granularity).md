# init(_:affinity:granularity:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a new text selection with the ranges, selection affinity, and granularity you provide.

**Availability**:
- macOS 12.0+

## Declaration

```swift
init(_ textRanges: [NSTextRange], affinity: NSTextSelection.Affinity, granularity: NSTextSelection.Granularity)
```

```objc
- (instancetype) initWithRanges:(NSArray<NSTextRange *> *) textRanges affinity:(NSTextSelectionAffinity) affinity granularity:(NSTextSelectionGranularity) granularity;
```

## Parameters

- `textRanges`: An array of text ranges.
- `affinity`: One of the available [`NSTextSelection.Affinity`](./affinity-swift.enum.md) options.
- `granularity`: One of the available [`NSTextSelection.Granularity`](./granularity-swift.enum.md) options.

## See Also

### Creating a text selection
- [convenience init(any NSTextLocation, affinity: NSTextSelection.Affinity)](./init%28_,affinity%29.md)
  Creates a new text selection with the location and selection affinity you provide.
- [convenience init(range: NSTextRange, affinity: NSTextSelection.Affinity, granularity: NSTextSelection.Granularity)](./init%28range,affinity,granularity%29.md)
  Creates a new text selection with the range, selection affinity, and granularity you provide.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a test selection from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselection/init(_:affinity:granularity:))*