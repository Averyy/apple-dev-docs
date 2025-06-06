# notifyPropertiesChanged(_:)

**Framework**: Core Media I/O  
**Kind**: method

Notifies connected clients of device property changes.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
func notifyPropertiesChanged(_ propertyStates: [CMIOExtensionProperty : CMIOExtensionPropertyState<AnyObject>])
```

## Parameters

- `propertyStates`: A dictionary of properties with changes.

## See Also

- [var connectedClients: [CMIOExtensionClient]](cmioextensionprovider/connectedclients.md)
  An array of connected clients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionprovider/notifypropertieschanged(_:))*