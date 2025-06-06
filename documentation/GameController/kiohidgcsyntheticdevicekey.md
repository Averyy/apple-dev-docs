# kIOHIDGCSyntheticDeviceKey

**Framework**: Game Controller  
**Kind**: var

A key that specifies whether the device is a game controller synthetic HID device.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var kIOHIDGCSyntheticDeviceKey: String { get }
```

## Mentions

- [Understanding game controller backward compatibility](understanding-game-controller-backward-compatibility.md)

#### Discussion

This key is present with a Boolean value of `true` on all game controller synthetic HID devices that the Game Controller framework creates.

If your app needs to exclude these synthetic HID devices from discovery by [`IOHIDManagerRef`](https://developer.apple.com/documentation/iokit/iohidmanagerref), [`IOServiceGetMatchingServices(_:_:_:)`](https://developer.apple.com/documentation/iokit/1514494-ioservicegetmatchingservices), or [`IOServiceAddMatchingNotification(_:_:_:_:_:_:)`](https://developer.apple.com/documentation/iokit/1514362-ioserviceaddmatchingnotification), include the [`kIOHIDGCSyntheticDeviceKey`](kiohidgcsyntheticdevicekey.md) with a value of `false` in the matching criteria.

```objc
IOHIDManagerRef manager = IOHIDManagerCreate(kCFAllocatorDefault, kIOHIDManagerOptionNone);
IOHIDManagerSetDeviceMatching(manager, (__bridge CFDictionaryRef)@{
    @kIOProviderClassKey: @kIOHIDDeviceKey,
    @kIOHIDGCSyntheticDeviceKey: @(NO)
});
```

Your code can check whether an [`io_service_t`](https://developer.apple.com/documentation/iokit/io_service_t) or an [`IOHIDDeviceRef`](https://developer.apple.com/documentation/iokit/iohiddeviceref) refers to a game controller synthetic HID device by querying the value of the [`kIOHIDGCSyntheticDeviceKey`](kiohidgcsyntheticdevicekey.md) property.

```objc
if ( IOHIDDeviceGetProperty(device, CFSTR(kIOHIDGCSyntheticDeviceKey)) == kCFBooleanTrue ) {
    // This is a synthetic HID device.
}
```

## See Also

- [Understanding game controller backward compatibility](understanding-game-controller-backward-compatibility.md)
  Learn how macOS brings support for the latest game controllers to software that predates the introduction of the Game Controller framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/kiohidgcsyntheticdevicekey)*