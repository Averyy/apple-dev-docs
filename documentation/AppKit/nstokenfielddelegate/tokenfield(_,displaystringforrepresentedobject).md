# tokenField(_:displayStringForRepresentedObject:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Allows the delegate to provide a string to be displayed as a proxy for the given represented object.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func tokenField(_ tokenField: NSTokenField, displayStringForRepresentedObject representedObject: Any) -> String?
```

```objc
- (NSString *) tokenField:(NSTokenField *) tokenField displayStringForRepresentedObject:(id) representedObject;
```

## Return Value

The string to be used as a proxy for `representedObject`. If you return `nil` or do not implement this method, then `representedObject` is displayed as the string.

## Parameters

- `tokenField`: The token field that sent the message.
- `representedObject`: A represented object of the token field.

## See Also

### Related Documentation
- [func tokenFieldCell(NSTokenFieldCell, displayStringForRepresentedObject: Any) -> String?](../nstokenfieldcelldelegate/tokenfieldcell%28_,displaystringforrepresentedobject%29.md)
  Allows the delegate to provide a string to be displayed as a proxy for the represented object.
### Displaying Tokenized Strings
- [func tokenField(NSTokenField, styleForRepresentedObject: Any) -> NSTokenField.TokenStyle](./tokenfield%28_,styleforrepresentedobject%29.md)
  Allows the delegate to return the token style for editing the specified represented object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstokenfielddelegate/tokenfield(_:displaystringforrepresentedobject:))*