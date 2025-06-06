# init(itemIdentifier:uiView:)

**Framework**: UIKit  
**Kind**: init

Creates a toolbar item with the identifier and underlying UIKit view you specify.

**Availability**:
- Mac Catalyst 16.0+

## Declaration

```swift
@MainActor
init(itemIdentifier identifier: NSToolbarItem.Identifier, uiView: UIView)
```

## Parameters

- `identifier`: The identifier for the toolbar item. You use this value to identify the item within your app, so you don’t need to localize it. For example, your toolbar delegate uses this value to identify the specific toolbar item.
- `uiView`: The UIKit view for the toolbar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsuiviewtoolbaritem/init(itemidentifier:uiview:))*