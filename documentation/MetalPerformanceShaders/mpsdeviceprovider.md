# MPSDeviceProvider

**Framework**: Metal Performance Shaders  
**Kind**: protocol  
**Role**: Protocol

An interface that enables the setting of a Metal device for unarchived objects.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
protocol MPSDeviceProvider
```

```objc
@protocol MPSDeviceProvider
```

## Topics

### Instance Methods
- [func mpsMTLDevice() -> (any MTLDevice)!](./mpsdeviceprovider/mpsmtldevice%28%29.md)

## Relationships

### Conforming Types
- [MPSKeyedUnarchiver](./mpskeyedunarchiver.md)

## See Also

### Keyed Archivers
- [class NSKeyedArchiver](../Foundation/nskeyedarchiver.md)
  An encoder that stores an object’s data to an archive referenced by keys.
- [class MPSKeyedUnarchiver](./mpskeyedunarchiver.md)
  A keyed archiver that supports Metal Performance Shaders kernel decoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsdeviceprovider)*