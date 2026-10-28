# servicesMenu

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The app’s Services menu.

**Availability**:
- macOS

## Declaration

```swift
var servicesMenu: NSMenu? { get set }
```

```objc
@property (strong, nullable) NSMenu * servicesMenu;
```

## Discussion

This property contains the app’s Services menu or `nil` if that menu has not been created. You can assign a new value to the property to set the Services menu for your app.

## See Also

### Managing the Services Menu
- [func registerServicesMenuSendTypes([NSPasteboard.PasteboardType], returnTypes: [NSPasteboard.PasteboardType])](./registerservicesmenusendtypes%28_,returntypes%29.md)
  Registers the pasteboard types the receiver can send and receive in response to service requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/servicesmenu)*