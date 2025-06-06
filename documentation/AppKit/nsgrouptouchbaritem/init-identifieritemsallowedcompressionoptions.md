# init(identifier:items:allowedCompressionOptions:)

**Framework**: AppKit  
**Kind**: init

Initializes and returns a group item whose bar is constructed from the supplied items, and with the specified compression options.

**Availability**:
- macOS 10.13+

## Declaration

```swift
@MainActor
convenience init(identifier: NSTouchBarItem.Identifier, items: [NSTouchBarItem], allowedCompressionOptions: NSUserInterfaceCompressionOptions)
```

#### Discussion

Use this initializer to specify which compression options are applied to the group item. The system applies options in the following default order: `breakEqualWidths`, `reduceMetrics`, `hideText`, `hideImages`.

If you want to use non-standard compression options, add them by using the [`prioritizedCompressionOptions`](nsgrouptouchbaritem/prioritizedcompressionoptions.md) property.

## See Also

- [convenience init(identifier: NSTouchBarItem.Identifier, items: [NSTouchBarItem])](nsgrouptouchbaritem/init(identifier:items:).md)
  Initializes and returns a group item whose bar is constructed from the supplied items.
- [convenience init(alertStyleWithIdentifier: NSTouchBarItem.Identifier)](nsgrouptouchbaritem/init(alertstylewithidentifier:).md)
  Initializes and returns a group item configured to match system alerts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgrouptouchbaritem/init(identifier:items:allowedcompressionoptions:))*