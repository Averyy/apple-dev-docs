# PlatformType.Value

**Framework**: LightweightCodeRequirements  
**Kind**: struct

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

#### Overview

A platform type is an indication of the runtime enviroment of a process. These runtime enviroments indicate the types of code that can run in the process, the dyld shared cache in use and impact some security policies.

## Topics

### Initializers
- [init?(rawValue: Int64)](platformtype/value/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Instance Properties
- [let rawValue: Int64](platformtype/value/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [PlatformType.Value.RawValue](platformtype/value/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Type Properties
- [static let driverKit: PlatformType.Value](platformtype/value/driverkit.md)
  The platform type for a driverkit driver.
- [static let iOS: PlatformType.Value](platformtype/value/ios.md)
  The platform type for iOS/iPadOS software running on iOS/ipadOS/macOS/visionOS
- [static let iOSSimulator: PlatformType.Value](platformtype/value/iossimulator.md)
  The platform type for code running in the iOS Simulator.
- [static let macCatalyst: PlatformType.Value](platformtype/value/maccatalyst.md)
  The platform type for macCatalyst software.
- [static let macOS: PlatformType.Value](platformtype/value/macos.md)
  The platform type for non-macCatalyst macOS software.
- [static let tvOS: PlatformType.Value](platformtype/value/tvos.md)
  The platform type for native tvOS software.
- [static let tvOSSimulator: PlatformType.Value](platformtype/value/tvossimulator.md)
  The platform type for code running in the tvOS Simulator.
- [static let visionOS: PlatformType.Value](platformtype/value/visionos.md)
  The platform type for native visionOS code.
- [static let visionOSSimulator: PlatformType.Value](platformtype/value/visionossimulator.md)
  The platform type for code running in the visionOS Simulator.
- [static let watchOS: PlatformType.Value](platformtype/value/watchos.md)
  The platform type for native watchOS software.
- [static let watchOSSimulator: PlatformType.Value](platformtype/value/watchossimulator.md)
  The platform type for code running in the watchOS Simulator.
### Default Implementations
- [Equatable Implementations](platformtype/value/equatable-implementations.md)
- [RawRepresentable Implementations](platformtype/value/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/platformtype/value)*