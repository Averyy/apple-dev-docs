# init(_:affinity:)

**Framework**: UIKit  
**Kind**: init

Creates a new text selection with the location and selection affinity you provide.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(_ location: any NSTextLocation, affinity: NSTextSelection.Affinity)
```

## Parameters

- `location`: The text location
- `affinity`: One of the possible   options.

## See Also

- [convenience init(range: NSTextRange, affinity: NSTextSelection.Affinity, granularity: NSTextSelection.Granularity)](nstextselection/init(range:affinity:granularity:).md)
  Creates a new text selection with the range, selection affinity, and granularity you provide.
- [init([NSTextRange], affinity: NSTextSelection.Affinity, granularity: NSTextSelection.Granularity)](nstextselection/init(_:affinity:granularity:).md)
  Creates a new text selection with the ranges, selection affinity, and granularity you provide.
- [init?(coder: NSCoder)](nstextselection/init(coder:).md)
  Creates a test selection from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextselection/init(_:affinity:))*