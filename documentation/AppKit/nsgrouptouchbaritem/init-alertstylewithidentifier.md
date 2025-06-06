# init(alertStyleWithIdentifier:)

**Framework**: AppKit  
**Kind**: init

Initializes and returns a group item configured to match system alerts.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.13+

## Declaration

```swift
@MainActor
convenience init(alertStyleWithIdentifier identifier: NSTouchBarItem.Identifier)
```

#### Discussion

You can control spacing between items, but it is recommended to use [`fixedSpaceLarge`](nstouchbaritem/identifier-swift.struct/fixedspacelarge.md) to maintain consistency.

The [`groupUserInterfaceLayoutDirection`](nsgrouptouchbaritem/groupuserinterfacelayoutdirection.md) is set to match the application’s [`userInterfaceLayoutDirection`](nsapplication/userinterfacelayoutdirection.md).

## See Also

- [convenience init(identifier: NSTouchBarItem.Identifier, items: [NSTouchBarItem])](nsgrouptouchbaritem/init(identifier:items:).md)
  Initializes and returns a group item whose bar is constructed from the supplied items.
- [convenience init(identifier: NSTouchBarItem.Identifier, items: [NSTouchBarItem], allowedCompressionOptions: NSUserInterfaceCompressionOptions)](nsgrouptouchbaritem/init(identifier:items:allowedcompressionoptions:).md)
  Initializes and returns a group item whose bar is constructed from the supplied items, and with the specified compression options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgrouptouchbaritem/init(alertstylewithidentifier:))*