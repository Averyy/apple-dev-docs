# init(named:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Returns a sharing service instance representing the specified service name.

**Availability**:
- macOS 10.8+

## Declaration

```swift
init?(named serviceName: NSSharingService.Name)
```

```objc
+ (NSSharingService *) sharingServiceNamed:(NSSharingServiceName) serviceName;
```

#### Return Value

An instance of `NSSharingService` for the specified service name.

## Parameters

- `serviceName`: The service name. The possible system provided values are listed in `Available Sharing Services`.

## See Also

### Related Documentation
- [class func sharingServices(forItems: [Any]) -> [NSSharingService]](./sharingservices%28foritems%29.md)
  Returns a list of sharing services which could share all the provided items together.
- [func canPerform(withItems: [Any]?) -> Bool](./canperform%28withitems%29.md)
  Returns whether the service can share all the specified items.
### Creating a Sharing Service
- [init(title: String, image: NSImage, alternateImage: NSImage?, handler: () -> Void)](./init%28title,image,alternateimage,handler%29.md)
  Creates a custom sharing service object.
- [NSSharingService.Name](./name.md)
  Constants that describe the sharing services that macOS supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservice/init(named:))*