# init(range:affinity:granularity:)

**Framework**: AppKit  
**Kind**: init

Creates a new text selection with the range, selection affinity, and granularity you provide.

**Availability**:
- macOS 12.0+

## Declaration

```swift
convenience init(range: NSTextRange, affinity: NSTextSelection.Affinity, granularity: NSTextSelection.Granularity)
```

## Parameters

- `range`: The range of the selection.
- `affinity`: One of the available   options.
- `granularity`: One of the available   options.

## See Also

- [convenience init(any NSTextLocation, affinity: NSTextSelection.Affinity)](nstextselection/init(_:affinity:).md)
  Creates a new text selection with the location and selection affinity you provide.
- [init([NSTextRange], affinity: NSTextSelection.Affinity, granularity: NSTextSelection.Granularity)](nstextselection/init(_:affinity:granularity:).md)
  Creates a new text selection with the ranges, selection affinity, and granularity you provide.
- [init?(coder: NSCoder)](nstextselection/init(coder:).md)
  Creates a test selection from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselection/init(range:affinity:granularity:))*