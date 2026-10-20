# ValidationCategory.Value

**Framework**: LightweightCodeRequirements  
**Kind**: struct  
**Role**: Structure

Supported Validation categories for signatures

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

## Topics

### Initializers
- [init?(rawValue: Int64)](./value/init%28rawvalue%29.md)
  Creates a new instance with the specified raw value.
### Instance Properties
- [let rawValue: Int64](./value/rawvalue.md)
  The corresponding value of the raw type.
### Type Properties
- [static let appStore: ValidationCategory.Value](./value/appstore.md)
  Indicates that the code is signed by Apple’s App Store
- [static let developerID: ValidationCategory.Value](./value/developerid.md)
  Indicates that the code is signed by an Apple issued Developer ID certificate.
- [static let development: ValidationCategory.Value](./value/development.md)
  Indicates that the code is signed by an Apple issued development certificate.
- [static let enterprise: ValidationCategory.Value](./value/enterprise.md)
  Indicates that the code is signed by an Apple issued distribution certificate and allowed to run via Provisioning profile.
- [static let none: ValidationCategory.Value](./value/none.md)
  Indicates that the code is either adhoc signed or signed by an un-recognized certificate chain.
- [static let platform: ValidationCategory.Value](./value/platform.md)
  Indicates that the code is signed by Apple or allowed by a loaded trustcache.
- [static let testflight: ValidationCategory.Value](./value/testflight.md)
  Indicates that the code is signed by Apple’s TestFlight certificate

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

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/validationcategory/value)*