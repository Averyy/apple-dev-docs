# init(_:affinity:granularity:)

**Framework**: UIKit  
**Kind**: init

Creates a new text selection with the ranges, selection affinity, and granularity you provide.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextselection/init(_:affinity:granularity:))*