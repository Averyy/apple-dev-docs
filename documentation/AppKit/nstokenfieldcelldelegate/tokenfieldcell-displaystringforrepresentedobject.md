# tokenFieldCell(_:displayStringForRepresentedObject:)

**Framework**: AppKit  
**Kind**: method

Allows the delegate to provide a string to be displayed as a proxy for the represented object.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func tokenFieldCell(_ tokenFieldCell: NSTokenFieldCell, displayStringForRepresentedObject representedObject: Any) -> String?
```

#### Return Value

The string to be used as a proxy for `representedObject`. If you return `nil` or do not implement this method, then `representedObject` is displayed as the string.

## Parameters

- `tokenFieldCell`: The token field cell that sent the message.
- `representedObject`: A represented object of the token field cell.

## See Also

- [Token Field Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TokenField_Guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40006555)
- [func tokenFieldCell(NSTokenFieldCell, styleForRepresentedObject: Any) -> NSTokenField.TokenStyle](nstokenfieldcelldelegate/tokenfieldcell(_:styleforrepresentedobject:).md)
  Allows the delegate to return the token style for editing the specified represented object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstokenfieldcelldelegate/tokenfieldcell(_:displaystringforrepresentedobject:))*