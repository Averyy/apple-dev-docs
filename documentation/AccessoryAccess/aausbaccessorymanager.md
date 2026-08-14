# AAUSBAccessoryManager

**Framework**: Accessory Access  
**Kind**: class

A class your app uses to manage USB accessories and the listener objects for those accessories.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class AAUSBAccessoryManager
```

#### Discussion

Don’t instantiate an `AAUSBAccessoryManager` directly, instead obtain the manager through the class property [`shared`](aausbaccessorymanager/shared.md).

Use the `AAUSBAccessoryManager` to manage accessories and register interest in events from USB accessories through [`AAUSBAccessoryListener`](aausbaccessorylistener.md) objects.  When a USB accessory connects to the system, the USB accessory manager notifies the listener and provides it an [`AAUSBAccessory`](aausbaccessory.md) object that represents this accessory. Your app can open this [`AAUSBAccessory`](aausbaccessory.md) object exclusively, and use it for performing USB transfers to the connected accessory.

A USB accessory listener receives notifications when a USB accessories connect to or disconnect from the system. These listeners can register or unregister with the USB accessory manager object. The accessory manager notifies your app about the USB accessories as long an accessory’s listener remains registered with the manager. The framework delivers all the notifications to the listener on the internal serial queue of the accessory manager.

The `AAUSBAccessoryManager` presents UI on behalf of your application, which means you can only use it from an application that implements a UI, that is, one that appears in the Dock.

> **Note**: To use the AccessoryAccess framework, add the `com.apple.developer.accessory-access.usb` entitlement to your app’s Xcode configuration. For more information, see [`Accessory Access`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.accessory-access.usb).

## Topics

### Accessing the shared manager
- [class var shared: AAUSBAccessoryManager](aausbaccessorymanager/shared.md)
  Returns the shared USB accessory manager object for this process.
### Registering and unregistering listeners
- [func registerListener(any AAUSBAccessoryListener, matchingCriteria: [AAUSBAccessoryMatchingCriteria], completionHandler: ([AAUSBAccessory], (any Error)?) -> Void)](aausbaccessorymanager/registerlistener(_:matchingcriteria:completionhandler:).md)
  Registers a USB accessory listener.
- [func unregisterListener(any AAUSBAccessoryListener, completionHandler: () -> Void)](aausbaccessorymanager/unregisterlistener(_:completionhandler:).md)
  Unregister a previously registered listener.
### Finding events that apply to an accessory
- [func events(matching: [AAUSBAccessoryMatchingCriteria]) async throws -> some AsyncSequence<AAUSBAccessory.Event, Never>
](aausbaccessorymanager/events(matching:).md)
  Returns an asynchronous list of events that match the provided criteria.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class AAUSBAccessory](aausbaccessory.md)
  A class that represents a USB accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryaccess/aausbaccessorymanager)*