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

### Instance Properties
- [var initialCapacity: Int](avprovideostorage/initialcapacity.md)
  Initial size of Pro Video Storage in bytes.
- [var isBusy: Bool](avprovideostorage/isbusy.md)
  Indicates whether Pro Video Storage is currently busy.
- [var remainingCapacity: Int](avprovideostorage/remainingcapacity.md)
  Current size of Pro Video Storage in bytes.
### Instance Methods
- [func openSettings()](avprovideostorage/opensettings.md)
  Opens the Pro Video Storage UI in Settings app.
### Type Properties
- [class var isSupported: Bool](avprovideostorage/issupported.md)
  Whether Pro Video Storage is supported in its current configuration.
- [class var shared: AVProVideoStorage?](avprovideostorage/shared.md)
  Returns the singleton instance for Pro Video Storage.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avprovideostorage)*