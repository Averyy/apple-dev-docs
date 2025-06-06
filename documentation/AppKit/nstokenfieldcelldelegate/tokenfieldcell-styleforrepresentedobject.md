# tokenFieldCell(_:styleForRepresentedObject:)

**Framework**: AppKit  
**Kind**: method

Allows the delegate to return the token style for editing the specified represented object.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func tokenFieldCell(_ tokenFieldCell: NSTokenFieldCell, styleForRepresentedObject representedObject: Any) -> NSTokenField.TokenStyle
```

#### Return Value

The style that should be used to display the representedObject. Possible values are shown in NSTokenStyle_Values.

#### Discussion

If the delegate implements this method and returns an [`NSTokenField.TokenStyle`](nstokenfield/tokenstyle-swift.enum.md) that differs from the style set by [`tokenStyle`](nstokenfieldcell/tokenstyle.md), the value the delegate returns is preferred.

If the delegate does not implement this method, the token field cell’s [`tokenStyle`](nstokenfieldcell/tokenstyle.md) is used.

## Parameters

- `tokenFieldCell`: The token field cell that sent the message.
- `representedObject`: A represented object of the token field cell.

## See Also

- [func tokenFieldCell(NSTokenFieldCell, displayStringForRepresentedObject: Any) -> String?](nstokenfieldcelldelegate/tokenfieldcell(_:displaystringforrepresentedobject:).md)
  Allows the delegate to provide a string to be displayed as a proxy for the represented object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstokenfieldcelldelegate/tokenfieldcell(_:styleforrepresentedobject:))*