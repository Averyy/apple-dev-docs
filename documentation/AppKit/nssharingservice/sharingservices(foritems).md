# sharingServices(forItems:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns a list of sharing services which could share all the provided items together.

**Availability**:
- macOS 10.8+ - Deprecated in 13.0

> **Deprecated**: Use -[NSSharingServicePicker standardShareMenuItem] instead.

## Declaration

```swift
class func sharingServices(forItems items: [Any]) -> [NSSharingService]
```

```objc
+ (NSArray<NSSharingService *> *) sharingServicesForItems:(NSArray *) items;
```

## Return Value

An array of sharing services to allow for `items`.

## Discussion

This method can be used to build a custom user interface or to populate a contextual menu.

## Parameters

- `items`: The items to share.

## See Also

### Related Documentation
- [init?(named: NSSharingService.Name)](./init%28named%29.md)
  Returns a sharing service instance representing the specified service name.
### Querying Service Availability
- [func canPerform(withItems: [Any]?) -> Bool](./canperform%28withitems%29.md)
  Returns whether the service can share all the specified items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservice/sharingservices(foritems:))*