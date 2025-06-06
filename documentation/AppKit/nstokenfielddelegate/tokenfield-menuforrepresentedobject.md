# tokenField(_:menuForRepresentedObject:)

**Framework**: AppKit  
**Kind**: method

Allows the delegate to provide a menu for the specified represented object.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func tokenField(_ tokenField: NSTokenField, menuForRepresentedObject representedObject: Any) -> NSMenu?
```

#### Return Value

The menu associated with the  represented object.

#### Discussion

The returned menu should be autoreleased. By default tokens in a token field do not return menus.

## Parameters

- `tokenField`: The token field that sent the message.
- `representedObject`: A represented object of the token field.

## See Also

- [func tokenField(NSTokenField, hasMenuForRepresentedObject: Any) -> Bool](nstokenfielddelegate/tokenfield(_:hasmenuforrepresentedobject:).md)
  Allows the delegate to specify whether the given represented object provides a menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstokenfielddelegate/tokenfield(_:menuforrepresentedobject:))*