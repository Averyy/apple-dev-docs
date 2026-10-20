# tokenFieldCell(_:hasMenuForRepresentedObject:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Allows the delegate to specify whether the represented object provides a menu.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func tokenFieldCell(_ tokenFieldCell: NSTokenFieldCell, hasMenuForRepresentedObject representedObject: Any) -> Bool
```

```objc
- (BOOL) tokenFieldCell:(NSTokenFieldCell *) tokenFieldCell hasMenuForRepresentedObject:(id) representedObject;
```

#### Return Value

[`true`](../../Swift/true.md) if the  represented object has a menu, [`false`](../../Swift/false.md) otherwise.

#### Discussion

By default tokens have no menus.

## Parameters

- `tokenFieldCell`: The token field cell that sent the message.
- `representedObject`: A represented object of the token field.

## See Also

### Managing Menus for Represented Objects
- [func tokenFieldCell(NSTokenFieldCell, menuForRepresentedObject: Any) -> NSMenu?](./tokenfieldcell%28_,menuforrepresentedobject%29.md)
  Allows the delegate to provide a menu for the specified represented object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstokenfieldcelldelegate/tokenfieldcell(_:hasmenuforrepresentedobject:))*