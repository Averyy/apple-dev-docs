# sharingService(_:didFailToShareItems:error:)

**Framework**: AppKit  
**Kind**: method

Invoked when the sharing service encountered an error when sharing items.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
optional func sharingService(_ sharingService: NSSharingService, didFailToShareItems items: [Any], error: any Error)
```

## Parameters

- `sharingService`: The sharing service.
- `items`: The items being shared.
- `error`: The error that was encountered when trying to share the item. If the error is  , the user simply cancelled the error.

## See Also

- [func sharingService(NSSharingService, willShareItems: [Any])](nssharingservicedelegate/sharingservice(_:willshareitems:).md)
  Invoked when the sharing service will share the specified items.
- [func sharingService(NSSharingService, didShareItems: [Any])](nssharingservicedelegate/sharingservice(_:didshareitems:).md)
  Invoked when the sharing service has finished sharing the items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservicedelegate/sharingservice(_:didfailtoshareitems:error:))*