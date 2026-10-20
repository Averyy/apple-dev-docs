# init(coder:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a test selection from data in an unarchiver.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
init?(coder: NSCoder)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) coder;
```

## Parameters

- `coder`: A coder that subclasses [`NSCoder`](../../Foundation/nscoder.md).

## See Also

### Creating a text selection
- [convenience init(any NSTextLocation, affinity: NSTextSelection.Affinity)](./init%28_,affinity%29.md)
  Creates a new text selection with the location and selection affinity you provide.
- [convenience init(range: NSTextRange, affinity: NSTextSelection.Affinity, granularity: NSTextSelection.Granularity)](./init%28range,affinity,granularity%29.md)
  Creates a new text selection with the range, selection affinity, and granularity you provide.
- [init([NSTextRange], affinity: NSTextSelection.Affinity, granularity: NSTextSelection.Granularity)](./init%28_,affinity,granularity%29.md)
  Creates a new text selection with the ranges, selection affinity, and granularity you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextselection/init(coder:))*