# notifyPropertiesChanged(_:)

**Framework**: Core Media I/O  
**Kind**: method  
**Role**: Instance Method

Notifies connected clients of device property changes.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
func notifyPropertiesChanged(_ propertyStates: [CMIOExtensionProperty : CMIOExtensionPropertyState<AnyObject>])
```

```objc
- (void) notifyPropertiesChanged:(NSDictionary<NSString *,CMIOExtensionPropertyState *> *) propertyStates;
```

## Parameters

- `propertyStates`: A dictionary of properties with changes.

## See Also

### Managing Clients
- [var connectedClients: [CMIOExtensionClient]](./connectedclients.md)
  An array of connected clients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionprovider/notifypropertieschanged(_:))*