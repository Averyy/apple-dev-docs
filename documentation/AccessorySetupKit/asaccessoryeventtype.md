# ASAccessoryEventType

**Framework**: AccessorySetupKit  
**Kind**: enum  
**Role**: Enumeration

An enumeration of the types of events encountered during accessory discovery

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst

## Declaration

```swift
enum ASAccessoryEventType
```

```c
enum ASAccessoryEventType : NSInteger;
```

## Topics

### Creating an event type instance
- [init?(rawValue: Int)](./asaccessoryeventtype/init%28rawvalue%29.md)
### Accessory events
- [ASAccessoryEventType.accessoryAdded](./asaccessoryeventtype/accessoryadded.md)
  The session added an accessory.
- [ASAccessoryEventType.accessoryChanged](./asaccessoryeventtype/accessorychanged.md)
  The properties of an accessory changed.
- [ASAccessoryEventType.accessoryRemoved](./asaccessoryeventtype/accessoryremoved.md)
  The session removed an accessory.
### Life cycle events
- [ASAccessoryEventType.activated](./asaccessoryeventtype/activated.md)
  The discovery session activated.
- [ASAccessoryEventType.invalidated](./asaccessoryeventtype/invalidated.md)
  The discovery session invalidated.
### Discovery events
- [ASAccessoryEventType.accessoryDiscovered](./asaccessoryeventtype/accessorydiscovered.md)
  The session discovered an accessory.
### Picker events
- [ASAccessoryEventType.pickerDidPresent](./asaccessoryeventtype/pickerdidpresent.md)
  The discovery session picker appeared.
- [ASAccessoryEventType.pickerDidDismiss](./asaccessoryeventtype/pickerdiddismiss.md)
  The discovery session picker dismissed.
- [ASAccessoryEventType.pickerSetupBridging](./asaccessoryeventtype/pickersetupbridging.md)
  The discovery session picker started bridging with an accessory.
- [ASAccessoryEventType.pickerSetupPairing](./asaccessoryeventtype/pickersetuppairing.md)
  The discovery session picker started pairing with a Bluetooth accessory.
- [ASAccessoryEventType.pickerSetupFailed](./asaccessoryeventtype/pickersetupfailed.md)
  The discovery session picker setup failed.
- [ASAccessoryEventType.pickerSetupRename](./asaccessoryeventtype/pickersetuprename.md)
  The discovery session picker started renaming an accessory.
### Migration events
- [ASAccessoryEventType.migrationComplete](./asaccessoryeventtype/migrationcomplete.md)
  The migration of an accessory completed.
### Unclassified events
- [ASAccessoryEventType.unknown](./asaccessoryeventtype/unknown.md)
  An unknown event occurred.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accessory discovery
- [class ASAccessoryEvent](./asaccessoryevent.md)
  Properties of an event encountered during accessory discovery.
- [class ASDiscoveryDescriptor](./asdiscoverydescriptor.md)
  Descriptive traits used to discover accessories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asaccessoryeventtype)*