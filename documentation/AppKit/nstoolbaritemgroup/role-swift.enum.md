# NSToolbarItemGroup.Role

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
enum Role
```

```c
enum NSToolbarItemGroupRole : NSInteger;
```

## Topics

### Getting role values
- [NSToolbarItemGroup.Role.automatic](./role-swift.enum/automatic.md)
- [NSToolbarItemGroup.Role.tabs](./role-swift.enum/tabs.md)
- [NSToolbarItemGroup.Role.valueSelection](./role-swift.enum/valueselection.md)
### Initializers
- [init?(rawValue: Int)](./role-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring grouped toolbar items
- [var controlRepresentation: NSToolbarItemGroup.ControlRepresentation](./controlrepresentation-swift.property.md)
  A value that represents how a toolbar displays a grouped toolbar item.
- [NSToolbarItemGroup.ControlRepresentation](./controlrepresentation-swift.enum.md)
- [var selectionMode: NSToolbarItemGroup.SelectionMode](./selectionmode-swift.property.md)
  The selection mode of the grouped toolbar item.
- [NSToolbarItemGroup.SelectionMode](./selectionmode-swift.enum.md)
  A value that indicates how a grouped toolbar item selects its subitems.
- [var role: NSToolbarItemGroup.Role](./role-swift.property.md)
  The semantic role of the item. Defaults to `NSToolbarItemGroupRoleAutomatic`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritemgroup/role-swift.enum)*