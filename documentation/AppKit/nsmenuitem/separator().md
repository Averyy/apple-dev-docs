# separator()

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns a menu item that is used to separate logical groups of menu commands.

**Availability**:
- macOS

## Declaration

```swift
class func separator() -> NSMenuItem
```

```objc
+ (NSMenuItem *) separatorItem;
```

#### Return Value

A menu item that is used to separate logical groups of menu commands.

#### Discussion

This menu item is disabled. The default separator item is blank space.

## See Also

### Related Documentation
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value that indicates whether the menu item is enabled.
### Managing the separator item
- [var isSeparatorItem: Bool](./isseparatoritem.md)
  A Boolean value indicating whether the menu item is a separator item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitem/separator())*