# servicesMenu

**Framework**: AppKit  
**Kind**: property

The app’s Services menu.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var servicesMenu: NSMenu? { get set }
```

#### Discussion

This property contains the app’s Services menu or `nil` if that menu has not been created. You can assign a new value to the property to set the Services menu for your app.

## See Also

- [func registerServicesMenuSendTypes([NSPasteboard.PasteboardType], returnTypes: [NSPasteboard.PasteboardType])](nsapplication/registerservicesmenusendtypes(_:returntypes:).md)
  Registers the pasteboard types the receiver can send and receive in response to service requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/servicesmenu)*