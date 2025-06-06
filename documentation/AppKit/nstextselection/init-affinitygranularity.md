# init(_:affinity:granularity:)

**Framework**: AppKit  
**Kind**: init

Creates a new text selection with the ranges, selection affinity, and granularity you provide.

**Availability**:
- macOS 12.0+

## Declaration

```swift
init(_ textRanges: [NSTextRange], affinity: NSTextSelection.Affinity, granularity: NSTextSelection.Granularity)
```

## Parameters

- `textRanges`: An array of text ranges.
- `affinity`: One of the available   options.
- `granularity`: One of the available   options.

## See Also

- [convenience init(any NSTextLocation, affinity: NSTextSelection.Affinity)](nstextselection/init(_:affinity:).md)
  Creates a new text selection with the location and selection affinity you provide.
- [convenience init(range: NSTextRange, affinity: NSTextSelection.Affinity, granularity: NSTextSelection.Granularity)](nstextselection/init(range:affinity:granularity:).md)
  Creates a new text selection with the range, selection affinity, and granularity you provide.
- [init?(coder: NSCoder)](nstextselection/init(coder:).md)
  Creates a test selection from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselection/init(_:affinity:granularity:))*