# init(identifier:items:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes and returns a group item whose bar is constructed from the supplied items.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
convenience init(identifier: NSTouchBarItem.Identifier, items: [NSTouchBarItem])
```

```objc
+ (instancetype) groupItemWithIdentifier:(NSTouchBarItemIdentifier) identifier items:(NSArray<NSTouchBarItem *> *) items;
```

## See Also

### Creating a group
- [convenience init(identifier: NSTouchBarItem.Identifier, items: [NSTouchBarItem], allowedCompressionOptions: NSUserInterfaceCompressionOptions)](./init%28identifier,items,allowedcompressionoptions%29.md)
  Initializes and returns a group item whose bar is constructed from the supplied items, and with the specified compression options.
- [convenience init(alertStyleWithIdentifier: NSTouchBarItem.Identifier)](./init%28alertstylewithidentifier%29.md)
  Initializes and returns a group item configured to match system alerts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgrouptouchbaritem/init(identifier:items:))*