# DockKitError

**Framework**: DockKit  
**Kind**: enum

A list of errors that DockKit sends.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
enum DockKitError
```

## Topics

### Getting errors
- [DockKitError.invalidParameter](dockkiterror/invalidparameter.md)
  The supplied parameter is invalid.
- [DockKitError.notConnected](dockkiterror/notconnected.md)
  The dock accessory isn’t connected to a device.
- [DockKitError.notSupported](dockkiterror/notsupported.md)
  The method isn’t supported on a specific platform.
- [DockKitError.notSupportedByDevice](dockkiterror/notsupportedbydevice.md)
  The device doesn’t support the requested operation.
### Operators
- [static func == (DockKitError, DockKitError) -> Bool](dockkiterror/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [DockKitError.cameraTCCMissing](dockkiterror/cameratccmissing.md)
  The camera terms and conditions are missing.
- [DockKitError.frameRateTooHigh](dockkiterror/frameratetoohigh.md)
  The call rate for the method is too frequent.
- [DockKitError.frameRateTooLow](dockkiterror/frameratetoolow.md)
  The frame rate is too low to track an object.
- [DockKitError.noSubjectFound](dockkiterror/nosubjectfound.md)
  There is no subject in the video frame.
### Instance Properties
- [var hashValue: Int](dockkiterror/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](dockkiterror/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](dockkiterror/equatable-implementations.md)
- [Error Implementations](dockkiterror/error-implementations.md)
- [LocalizedError Implementations](dockkiterror/localizederror-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Controlling a DockKit accessory using your camera app](controlling-a-dockkit-accessory-using-your-camera-app.md)
  Follow subjects in real time using an iPhone that you mount on a DockKit accessory.
- [class DockAccessoryManager](dockaccessorymanager.md)
  Observe the state of dock accessories and enable or disable system tracking.
- [class DockAccessory](dockaccessory.md)
  Obtain accessory information and control tracking behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockkiterror)*