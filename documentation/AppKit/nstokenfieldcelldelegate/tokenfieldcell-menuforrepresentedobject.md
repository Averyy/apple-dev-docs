# tokenFieldCell(_:menuForRepresentedObject:)

**Framework**: AppKit  
**Kind**: method

Allows the delegate to provide a menu for the specified represented object.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func tokenFieldCell(_ tokenFieldCell: NSTokenFieldCell, menuForRepresentedObject representedObject: Any) -> NSMenu?
```

#### Return Value

The menu associated with the  represented object.

#### Discussion

The returned menu should be autoreleased. By default tokens in a token field cell do not return menus.

## Parameters

- `tokenFieldCell`: The token field cell that sent the message.
- `representedObject`: A represented object of the token field.

## See Also

- [func tokenFieldCell(NSTokenFieldCell, hasMenuForRepresentedObject: Any) -> Bool](nstokenfieldcelldelegate/tokenfieldcell(_:hasmenuforrepresentedobject:).md)
  Allows the delegate to specify whether the represented object provides a menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstokenfieldcelldelegate/tokenfieldcell(_:menuforrepresentedobject:))*