# tokenFieldCell(_:displayStringForRepresentedObject:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Allows the delegate to provide a string to be displayed as a proxy for the represented object.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func tokenFieldCell(_ tokenFieldCell: NSTokenFieldCell, displayStringForRepresentedObject representedObject: Any) -> String?
```

```objc
- (NSString *) tokenFieldCell:(NSTokenFieldCell *) tokenFieldCell displayStringForRepresentedObject:(id) representedObject;
```

#### Return Value

The string to be used as a proxy for `representedObject`. If you return `nil` or do not implement this method, then `representedObject` is displayed as the string.

## Parameters

- `tokenFieldCell`: The token field cell that sent the message.
- `representedObject`: A represented object of the token field cell.

## See Also

### Related Documentation
- [func tokenField(NSTokenField, displayStringForRepresentedObject: Any) -> String?](../nstokenfielddelegate/tokenfield%28_,displaystringforrepresentedobject%29.md)
  Allows the delegate to provide a string to be displayed as a proxy for the given represented object.
### Displaying Tokenized Strings
- [func tokenFieldCell(NSTokenFieldCell, styleForRepresentedObject: Any) -> NSTokenField.TokenStyle](./tokenfieldcell%28_,styleforrepresentedobject%29.md)
  Allows the delegate to return the token style for editing the specified represented object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstokenfieldcelldelegate/tokenfieldcell(_:displaystringforrepresentedobject:))*