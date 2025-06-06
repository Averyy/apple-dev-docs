# sharingServices(forItems:)

**Framework**: AppKit  
**Kind**: method

Returns a list of sharing services which could share all the provided items together.

**Availability**:
- macOS 10.8+

## Declaration

```swift
class func sharingServices(forItems items: [Any]) -> [NSSharingService]
```

#### Return Value

An array of sharing services to allow for `items`.

#### Discussion

This method can be used to build a custom user interface or to populate a contextual menu.

## Parameters

- `items`: The items to share.

## See Also

- [init?(named: NSSharingService.Name)](nssharingservice/init(named:).md)
  Returns a sharing service instance representing the specified service name.
- [func canPerform(withItems: [Any]?) -> Bool](nssharingservice/canperform(withitems:).md)
  Returns whether the service can share all the specified items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservice/sharingservices(foritems:))*