# canPerform(withItems:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns whether the service can share all the specified items.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func canPerform(withItems items: [Any]?) -> Bool
```

```objc
- (BOOL) canPerformWithItems:(NSArray *) items;
```

## Return Value

[`true`](../../Swift/true.md) if the service can share all the items; [`false`](../../Swift/false.md) otherwise. If `items` is `nil`, the method will return [`true`](../../Swift/true.md) when the service is configured.

## Discussion

This method can be used to validate a custom user interface such as a dedicated Twitter button.  Therefore you could call it once at launch time with `nil` items to check whether to display the button or not, and then with real items to enable and disable the button depending on the context or selection.

## Parameters

- `items`: The items to share.

## See Also

### Related Documentation
- [func perform(withItems: [Any])](./perform%28withitems%29.md)
  Manually performs the service on the provided items.
### Querying Service Availability
- [class func sharingServices(forItems: [Any]) -> [NSSharingService]](./sharingservices%28foritems%29.md)
  Returns a list of sharing services which could share all the provided items together.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservice/canperform(withitems:))*