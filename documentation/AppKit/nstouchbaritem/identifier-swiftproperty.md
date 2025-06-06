# identifier

**Framework**: AppKit  
**Kind**: property

The identifier for this item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
@MainActor
var identifier: NSTouchBarItem.Identifier { get }
```

#### Discussion

This read-only property returns the value the item was initialized with.

For all items other than spaces, this value must be globally unique.

## See Also

- [NSTouchBarItem.Identifier](nstouchbaritem/identifier-swift.struct.md)
  An identifier for an item in the Touch Bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouchbaritem/identifier-swift.property)*