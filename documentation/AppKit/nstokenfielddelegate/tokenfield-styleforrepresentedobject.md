# tokenField(_:styleForRepresentedObject:)

**Framework**: AppKit  
**Kind**: method

Allows the delegate to return the token style for editing the specified represented object.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func tokenField(_ tokenField: NSTokenField, styleForRepresentedObject representedObject: Any) -> NSTokenField.TokenStyle
```

#### Return Value

The style that should be used to display the representedObject. Possible values are shown in NSTokenStyle Values.

#### Discussion

If the delegate implements this method and returns an [`NSTokenField.TokenStyle`](nstokenfield/tokenstyle-swift.enum.md) that differs from the style set by [`tokenStyle`](nstokenfield/tokenstyle-swift.property.md), the value the delegate returns is preferred.

If the delegate does not implement this method, the token field’s [`tokenStyle`](nstokenfield/tokenstyle-swift.property.md) is used.

## Parameters

- `tokenField`: The token field that sent the message.
- `representedObject`: A represented object of the token field.

## See Also

- [func tokenField(NSTokenField, displayStringForRepresentedObject: Any) -> String?](nstokenfielddelegate/tokenfield(_:displaystringforrepresentedobject:).md)
  Allows the delegate to provide a string to be displayed as a proxy for the given represented object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstokenfielddelegate/tokenfield(_:styleforrepresentedobject:))*