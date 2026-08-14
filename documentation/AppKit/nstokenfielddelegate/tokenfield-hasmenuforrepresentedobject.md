# tokenField(_:hasMenuForRepresentedObject:)

**Framework**: AppKit  
**Kind**: method

Allows the delegate to specify whether the given represented object provides a menu.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func tokenField(_ tokenField: NSTokenField, hasMenuForRepresentedObject representedObject: Any) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the  represented object has a menu, [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

#### Discussion

By default tokens in a token field have no menus.

## Parameters

- `tokenField`: The token field that sent the message.
- `representedObject`: A represented object of the token field.

## See Also

- [func tokenField(NSTokenField, menuForRepresentedObject: Any) -> NSMenu?](nstokenfielddelegate/tokenfield(_:menuforrepresentedobject:).md)
  Allows the delegate to provide a menu for the specified represented object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstokenfielddelegate/tokenfield(_:hasmenuforrepresentedobject:))*