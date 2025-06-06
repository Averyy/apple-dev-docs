# init(named:)

**Framework**: AppKit  
**Kind**: init

Returns a sharing service instance representing the specified service name.

**Availability**:
- macOS 10.8+

## Declaration

```swift
init?(named serviceName: NSSharingService.Name)
```

#### Return Value

An instance of `NSSharingService` for the specified service name.

## Parameters

- `serviceName`: The service name. The possible system provided values are listed in  .

## See Also

- [class func sharingServices(forItems: [Any]) -> [NSSharingService]](nssharingservice/sharingservices(foritems:).md)
  Returns a list of sharing services which could share all the provided items together.
- [func canPerform(withItems: [Any]?) -> Bool](nssharingservice/canperform(withitems:).md)
  Returns whether the service can share all the specified items.
- [init(title: String, image: NSImage, alternateImage: NSImage?, handler: () -> Void)](nssharingservice/init(title:image:alternateimage:handler:).md)
  Creates a custom sharing service object.
- [NSSharingService.Name](nssharingservice/name.md)
  Constants that describe the sharing services that macOS supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservice/init(named:))*