# init(range:affinity:granularity:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a new text selection with the range, selection affinity, and granularity you provide.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(range: NSTextRange, affinity: NSTextSelection.Affinity, granularity: NSTextSelection.Granularity)
```

```objc
- (instancetype) initWithRange:(NSTextRange *) range affinity:(NSTextSelectionAffinity) affinity granularity:(NSTextSelectionGranularity) granularity;
```

## Parameters

- `range`: The range of the selection.
- `affinity`: One of the available [`NSTextSelection.Affinity`](./affinity-swift.enum.md) options.
- `granularity`: One of the available [`NSTextSelection.Granularity`](./granularity-swift.enum.md) options.

## See Also

### Creating a text selection
- [convenience init(any NSTextLocation, affinity: NSTextSelection.Affinity)](./init%28_,affinity%29.md)
  Creates a new text selection with the location and selection affinity you provide.
- [init([NSTextRange], affinity: NSTextSelection.Affinity, granularity: NSTextSelection.Granularity)](./init%28_,affinity,granularity%29.md)
  Creates a new text selection with the ranges, selection affinity, and granularity you provide.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a test selection from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextselection/init(range:affinity:granularity:))*