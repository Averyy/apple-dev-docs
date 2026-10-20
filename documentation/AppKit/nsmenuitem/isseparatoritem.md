# isSeparatorItem

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the menu item is a separator item.

**Availability**:
- macOS

## Declaration

```swift
var isSeparatorItem: Bool { get }
```

```objc
@property (readonly, getter=isSeparatorItem) BOOL separatorItem;
```

#### Discussion

This menu item is disabled. The default separator item is blank space.

## See Also

### Managing the separator item
- [class func separator() -> NSMenuItem](./separator%28%29.md)
  Returns a menu item that is used to separate logical groups of menu commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitem/isseparatoritem)*