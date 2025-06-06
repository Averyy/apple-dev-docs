# sharingService(_:didShareItems:)

**Framework**: AppKit  
**Kind**: method

Invoked when the sharing service has finished sharing the items.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
optional func sharingService(_ sharingService: NSSharingService, didShareItems items: [Any])
```

## Parameters

- `sharingService`: The sharing service.
- `items`: The items being shared.

## See Also

- [func sharingService(NSSharingService, willShareItems: [Any])](nssharingservicedelegate/sharingservice(_:willshareitems:).md)
  Invoked when the sharing service will share the specified items.
- [func sharingService(NSSharingService, didFailToShareItems: [Any], error: any Error)](nssharingservicedelegate/sharingservice(_:didfailtoshareitems:error:).md)
  Invoked when the sharing service encountered an error when sharing items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservicedelegate/sharingservice(_:didshareitems:))*