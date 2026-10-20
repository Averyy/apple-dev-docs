# notifyPropertiesChanged(_:)

**Framework**: Core Media I/O  
**Kind**: method  
**Role**: Instance Method

Notifies clients of property changes.

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

- `propertyStates`: A dictionary of changed properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensiondevice/notifypropertieschanged(_:))*