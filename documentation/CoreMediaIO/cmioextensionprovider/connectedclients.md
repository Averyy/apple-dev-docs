# connectedClients

**Framework**: Core Media I/O  
**Kind**: property  
**Role**: Instance Property

An array of connected clients.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
var connectedClients: [CMIOExtensionClient] { get }
```

```objc
@property (atomic, copy, readonly) NSArray<CMIOExtensionClient *> * connectedClients;
```

## Discussion

This property is key-value observable.

## See Also

### Managing Clients
- [func notifyPropertiesChanged([CMIOExtensionProperty : CMIOExtensionPropertyState<AnyObject>])](./notifypropertieschanged%28_%29.md)
  Notifies connected clients of device property changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionprovider/connectedclients)*