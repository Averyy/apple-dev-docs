# init(coder:)

**Framework**: AppKit  
**Kind**: init

Creates a test selection from data in an unarchiver.

**Availability**:
- macOS 12.0+

## Declaration

```swift
init?(coder: NSCoder)
```

## Parameters

- `coder`: A coder that subclasses  .

## See Also

- [convenience init(any NSTextLocation, affinity: NSTextSelection.Affinity)](nstextselection/init(_:affinity:).md)
  Creates a new text selection with the location and selection affinity you provide.
- [convenience init(range: NSTextRange, affinity: NSTextSelection.Affinity, granularity: NSTextSelection.Granularity)](nstextselection/init(range:affinity:granularity:).md)
  Creates a new text selection with the range, selection affinity, and granularity you provide.
- [init([NSTextRange], affinity: NSTextSelection.Affinity, granularity: NSTextSelection.Granularity)](nstextselection/init(_:affinity:granularity:).md)
  Creates a new text selection with the ranges, selection affinity, and granularity you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselection/init(coder:))*