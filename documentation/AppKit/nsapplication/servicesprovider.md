# servicesProvider

**Framework**: AppKit  
**Kind**: property

The object that provides the services the current app advertises in the Services menu of other apps.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var servicesProvider: Any? { get set }
```

#### Return Value

The app’s service provider object.

#### Discussion

The service provider performs all advertised services for the app. When another app requests a service from the current app, the app object forwards the request to its service provider. Service requests can arrive immediately after the service provider is set, so assign an object to this property only when your app is ready to receive requests.

## See Also

- [func validRequestor(forSendType: NSPasteboard.PasteboardType?, returnType: NSPasteboard.PasteboardType?) -> Any?](nsapplication/validrequestor(forsendtype:returntype:).md)
  Indicates whether the receiver can send and receive the specified pasteboard types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/servicesprovider)*