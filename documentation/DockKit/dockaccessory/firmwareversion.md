# firmwareVersion

**Framework**: DockKit  
**Kind**: property  
**Role**: Instance Property

The firmware version of the dock accessory.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
final var firmwareVersion: String? { get }
```

#### Discussion

The format of the version is major, minor, and revision, separated by periods.

## See Also

### Getting accessory information
- [var hardwareModel: String?](./hardwaremodel.md)
  The model of the dock accessory.
- [let identifier: DockAccessory.Identifier](./identifier-swift.property.md)
  The name and unique identifer of the dock accessory.
- [DockAccessory.Identifier](./identifier-swift.struct.md)
  Information that uniquely identifies the dock accessory.
- [DockAccessory.Category](./category.md)
  Types of supported dock accesories.
- [DockAccessory.State](./state.md)
  The state of a dock accessory.
- [DockAccessory.StateChange](./statechange.md)
  An event that indicates a change in the state of a dock accessory.
- [DockAccessory.StateChanges](./statechanges.md)
  An asynchronous sequence of dock accessory state changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/firmwareversion)*