# HIDDeviceClient.UnsafeProperty

**Framework**: Core HID  
**Kind**: struct

A wrapper around an object to facilitate working with subscripts.

**Availability**:
- macOS 15.0+

## Declaration

```swift
struct UnsafeProperty
```

#### Overview

Note that this is unchecked Sendable, and therefore unsafe. The contained object is NOT guaranted to be concurrency safe.

## Topics

### Instance Properties
- [let unsafeObject: AnyObject](hiddeviceclient/unsafeproperty/unsafeobject.md)
  An object may not be safe to use concurrently.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddeviceclient/unsafeproperty)*