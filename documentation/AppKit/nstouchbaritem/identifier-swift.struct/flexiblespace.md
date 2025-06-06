# flexibleSpace

**Framework**: AppKit  
**Kind**: property

The identifier of an item appropriate for use as a flexible space in a Touch Bar.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
static let flexibleSpace: NSTouchBarItem.Identifier
```

#### Discussion

Use this identifier in the [`itemIdentifiers`](nstouchbar/itemidentifiers.md) array on an [`NSTouchBar`](nstouchbar.md) object and the system will instantiate the item for you.

## See Also

- [static let fixedSpaceSmall: NSTouchBarItem.Identifier](nstouchbaritem/identifier-swift.struct/fixedspacesmall.md)
  The identifier of an item appropriate for use as a small space in a Touch Bar.
- [static let fixedSpaceLarge: NSTouchBarItem.Identifier](nstouchbaritem/identifier-swift.struct/fixedspacelarge.md)
  The identifier of an item appropriate for use as a large space in a Touch Bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouchbaritem/identifier-swift.struct/flexiblespace)*