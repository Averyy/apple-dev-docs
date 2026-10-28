# init(alertStyleWithIdentifier:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes and returns a group item configured to match system alerts.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.13+

## Declaration

```swift
convenience init(alertStyleWithIdentifier identifier: NSTouchBarItem.Identifier)
```

```objc
+ (instancetype) alertStyleGroupItemWithIdentifier:(NSTouchBarItemIdentifier) identifier;
```

## Discussion

You can control spacing between items, but it is recommended to use [`fixedSpaceLarge`](../nstouchbaritem/identifier-swift.struct/fixedspacelarge.md) to maintain consistency.

The [`groupUserInterfaceLayoutDirection`](./groupuserinterfacelayoutdirection.md) is set to match the application’s [`userInterfaceLayoutDirection`](../nsapplication/userinterfacelayoutdirection.md).

## See Also

### Creating a group
- [convenience init(identifier: NSTouchBarItem.Identifier, items: [NSTouchBarItem])](./init%28identifier,items%29.md)
  Initializes and returns a group item whose bar is constructed from the supplied items.
- [convenience init(identifier: NSTouchBarItem.Identifier, items: [NSTouchBarItem], allowedCompressionOptions: NSUserInterfaceCompressionOptions)](./init%28identifier,items,allowedcompressionoptions%29.md)
  Initializes and returns a group item whose bar is constructed from the supplied items, and with the specified compression options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgrouptouchbaritem/init(alertstylewithidentifier:))*