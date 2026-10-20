# fixedSpaceSmall

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The identifier of an item appropriate for use as a small space in a Touch Bar.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
static let fixedSpaceSmall: NSTouchBarItem.Identifier
```

```c
extern NSTouchBarItemIdentifier const NSTouchBarItemIdentifierFixedSpaceSmall;
```

#### Discussion

Use this identifier in the [`itemIdentifiers`](../../nstouchbar/itemidentifiers.md) array on an [`NSTouchBar`](../../nstouchbar.md) object and the system will instantiate the item for you.

## See Also

### Creating identifiers for space items
- [static let fixedSpaceLarge: NSTouchBarItem.Identifier](./fixedspacelarge.md)
  The identifier of an item appropriate for use as a large space in a Touch Bar.
- [static let flexibleSpace: NSTouchBarItem.Identifier](./flexiblespace.md)
  The identifier of an item appropriate for use as a flexible space in a Touch Bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouchbaritem/identifier-swift.struct/fixedspacesmall)*