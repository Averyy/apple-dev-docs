# itemIdentifier

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The value you use to identify the toolbar item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS

## Declaration

```swift
var itemIdentifier: NSToolbarItem.Identifier { get }
```

```objc
@property (copy, readonly) NSToolbarItemIdentifier itemIdentifier;
```

## Discussion

Use this property to distinguish one toolbar item from another on the same toolbar.

## See Also

### Related Documentation
- [init(itemIdentifier: NSToolbarItem.Identifier)](./init%28itemidentifier%29.md)
  Creates a toolbar item with the specified identifier.
### Getting the toolbar item’s identity
- [NSToolbarItem.Identifier](./identifier.md)
  Constants for the standard toolbar items that the system provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritem/itemidentifier)*