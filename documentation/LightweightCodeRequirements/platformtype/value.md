# PlatformType.Value

**Framework**: LightweightCodeRequirements  
**Kind**: struct  
**Role**: Structure

Supported Platform Types for a process

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
struct Value
```

## Overview

A platform type is an indication of the runtime enviroment of a process. These runtime enviroments indicate the types of code that can run in the process, the dyld shared cache in use and impact some security policies.

## Topics

### Initializers
- [init?(rawValue: Int64)](./value/init%28rawvalue%29.md)
  Creates a new instance with the specified raw value.
### Instance Properties
- [let rawValue: Int64](./value/rawvalue.md)
  The corresponding value of the raw type.
### Type Properties
- [static let driverKit: PlatformType.Value](./value/driverkit.md)
  The platform type for a driverkit driver.
- [static let iOS: PlatformType.Value](./value/ios.md)
  The platform type for iOS/iPadOS software running on iOS/ipadOS/macOS/visionOS
- [static let iOSSimulator: PlatformType.Value](./value/iossimulator.md)
  The platform type for code running in the iOS Simulator.
- [static let macCatalyst: PlatformType.Value](./value/maccatalyst.md)
  The platform type for macCatalyst software.
- [static let macOS: PlatformType.Value](./value/macos.md)
  The platform type for non-macCatalyst macOS software.
- [static let tvOS: PlatformType.Value](./value/tvos.md)
  The platform type for native tvOS software.
- [static let tvOSSimulator: PlatformType.Value](./value/tvossimulator.md)
  The platform type for code running in the tvOS Simulator.
- [static let visionOS: PlatformType.Value](./value/visionos.md)
  The platform type for native visionOS code.
- [static let visionOSSimulator: PlatformType.Value](./value/visionossimulator.md)
  The platform type for code running in the visionOS Simulator.
- [static let watchOS: PlatformType.Value](./value/watchos.md)
  The platform type for native watchOS software.
- [static let watchOSSimulator: PlatformType.Value](./value/watchossimulator.md)
  The platform type for code running in the watchOS Simulator.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/platformtype/value)*