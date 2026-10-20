# sharingService(_:willShareItems:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked when the sharing service will share the specified items.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
optional func sharingService(_ sharingService: NSSharingService, willShareItems items: [Any])
```

```objc
- (void) sharingService:(NSSharingService *) sharingService willShareItems:(NSArray *) items;
```

## Parameters

- `sharingService`: The sharing service.
- `items`: The items being shared.

## See Also

### Sharing Items
- [func sharingService(NSSharingService, didShareItems: [Any])](./sharingservice%28_,didshareitems%29.md)
  Invoked when the sharing service has finished sharing the items.
- [func sharingService(NSSharingService, didFailToShareItems: [Any], error: any Error)](./sharingservice%28_,didfailtoshareitems,error%29.md)
  Invoked when the sharing service encountered an error when sharing items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservicedelegate/sharingservice(_:willshareitems:))*