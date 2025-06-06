# tokenField(_:displayStringForRepresentedObject:)

**Framework**: AppKit  
**Kind**: method

Allows the delegate to provide a string to be displayed as a proxy for the given represented object.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func tokenField(_ tokenField: NSTokenField, displayStringForRepresentedObject representedObject: Any) -> String?
```

#### Return Value

The string to be used as a proxy for `representedObject`. If you return `nil` or do not implement this method, then `representedObject` is displayed as the string.

## Parameters

- `tokenField`: The token field that sent the message.
- `representedObject`: A represented object of the token field.

## See Also

- [Token Field Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TokenField_Guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40006555)
- [func tokenField(NSTokenField, styleForRepresentedObject: Any) -> NSTokenField.TokenStyle](nstokenfielddelegate/tokenfield(_:styleforrepresentedobject:).md)
  Allows the delegate to return the token style for editing the specified represented object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstokenfielddelegate/tokenfield(_:displaystringforrepresentedobject:))*