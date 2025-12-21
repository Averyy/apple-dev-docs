# tokenFieldCell(_:hasMenuForRepresentedObject:)

**Framework**: AppKit  
**Kind**: method

Allows the delegate to specify whether the represented object provides a menu.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func tokenFieldCell(_ tokenFieldCell: NSTokenFieldCell, hasMenuForRepresentedObject representedObject: Any) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the  represented object has a menu, [`false`](https://developer.apple.com/documentation/Swift/false) otherwise.

#### Discussion

By default tokens have no menus.

## Parameters

- `tokenFieldCell`: The token field cell that sent the message.
- `representedObject`: A represented object of the token field.

## See Also

- [func tokenFieldCell(NSTokenFieldCell, menuForRepresentedObject: Any) -> NSMenu?](nstokenfieldcelldelegate/tokenfieldcell(_:menuforrepresentedobject:).md)
  Allows the delegate to provide a menu for the specified represented object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstokenfieldcelldelegate/tokenfieldcell(_:hasmenuforrepresentedobject:))*