# tokenField(_:hasMenuForRepresentedObject:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Allows the delegate to specify whether the given represented object provides a menu.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func tokenField(_ tokenField: NSTokenField, hasMenuForRepresentedObject representedObject: Any) -> Bool
```

```objc
- (BOOL) tokenField:(NSTokenField *) tokenField hasMenuForRepresentedObject:(id) representedObject;
```

## Return Value

[`true`](../../Swift/true.md) if the  represented object has a menu, [`false`](../../Swift/false.md) otherwise.

## Discussion

By default tokens in a token field have no menus.

## Parameters

- `tokenField`: The token field that sent the message.
- `representedObject`: A represented object of the token field.

## See Also

### Managing Menus for Represented Objects
- [func tokenField(NSTokenField, menuForRepresentedObject: Any) -> NSMenu?](./tokenfield%28_,menuforrepresentedobject%29.md)
  Allows the delegate to provide a menu for the specified represented object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstokenfielddelegate/tokenfield(_:hasmenuforrepresentedobject:))*