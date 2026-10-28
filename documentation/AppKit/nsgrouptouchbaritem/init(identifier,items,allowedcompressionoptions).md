# init(identifier:items:allowedCompressionOptions:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes and returns a group item whose bar is constructed from the supplied items, and with the specified compression options.

**Availability**:
- macOS 10.13+

## Declaration

```swift
convenience init(identifier: NSTouchBarItem.Identifier, items: [NSTouchBarItem], allowedCompressionOptions: NSUserInterfaceCompressionOptions)
```

```objc
+ (instancetype) groupItemWithIdentifier:(NSTouchBarItemIdentifier) identifier items:(NSArray<NSTouchBarItem *> *) items allowedCompressionOptions:(NSUserInterfaceCompressionOptions *) allowedCompressionOptions;
```

## Discussion

Use this initializer to specify which compression options are applied to the group item. The system applies options in the following default order: `breakEqualWidths`, `reduceMetrics`, `hideText`, `hideImages`.

If you want to use non-standard compression options, add them by using the [`prioritizedCompressionOptions`](./prioritizedcompressionoptions.md) property.

## See Also

### Creating a group
- [convenience init(identifier: NSTouchBarItem.Identifier, items: [NSTouchBarItem])](./init%28identifier,items%29.md)
  Initializes and returns a group item whose bar is constructed from the supplied items.
- [convenience init(alertStyleWithIdentifier: NSTouchBarItem.Identifier)](./init%28alertstylewithidentifier%29.md)
  Initializes and returns a group item configured to match system alerts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgrouptouchbaritem/init(identifier:items:allowedcompressionoptions:))*