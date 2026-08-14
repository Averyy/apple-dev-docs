# AVProVideoStorage

**Framework**: AVFoundation  
**Kind**: class

A class to track and manage pre-allocated storage for high data rate video capture.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)

## Declaration

```swift
class AVProVideoStorage
```

#### Overview

`AVProVideoStorage` is a singleton that manages system-wide pre-allocated storage used during high data rate video capture to ensure I/O determinism and sustain high bandwidth captures (e.g. ProRes).

## Topics

### Getting the shared storage
- [class var shared: AVProVideoStorage?](avprovideostorage/shared.md)
  Returns the singleton instance for Pro Video Storage.
- [class var isSupported: Bool](avprovideostorage/issupported.md)
  Whether Pro Video Storage is supported in its current configuration.
### Inspecting capacity
- [var initialCapacity: Int](avprovideostorage/initialcapacity.md)
  Initial size of Pro Video Storage in bytes.
- [var remainingCapacity: Int](avprovideostorage/remainingcapacity.md)
  Current size of Pro Video Storage in bytes.
- [func replenishCapacity(completionHandler: ((Int, (any Error)?) -> Void)?)](avprovideostorage/replenishcapacity(completionhandler:).md)
  Performs a best-effort attempt to restore Pro Video Storage to the initial capacity specified by the user in Settings app.
### Determining whether storage is busy
- [var busyReasons: Set<AVProVideoStorage.BusyReason>](avprovideostorage/busyreasons.md)
  Whether Pro Video Storage is busy and the associated reasons.
- [AVProVideoStorage.BusyReason](avprovideostorage/busyreason.md)
  A reason that Pro Video Storage may be busy.
### Presenting the settings interface
- [func openSettings()](avprovideostorage/opensettings.md)
  Opens the Pro Video Storage UI in Settings app.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avprovideostorage)*