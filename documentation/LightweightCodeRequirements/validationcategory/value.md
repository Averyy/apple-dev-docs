# ValidationCategory.Value

**Framework**: LightweightCodeRequirements  
**Kind**: struct

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
- [init?(rawValue: Int64)](validationcategory/value/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Instance Properties
- [let rawValue: Int64](validationcategory/value/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [ValidationCategory.Value.RawValue](validationcategory/value/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Type Properties
- [static let appStore: ValidationCategory.Value](validationcategory/value/appstore.md)
  Indicates that the code is signed by Apple’s App Store
- [static let developerID: ValidationCategory.Value](validationcategory/value/developerid.md)
  Indicates that the code is signed by an Apple issued Developer ID certificate.
- [static let development: ValidationCategory.Value](validationcategory/value/development.md)
  Indicates that the code is signed by an Apple issued development certificate.
- [static let enterprise: ValidationCategory.Value](validationcategory/value/enterprise.md)
  Indicates that the code is signed by an Apple issued distribution certificate and allowed to run via Provisioning profile.
- [static let none: ValidationCategory.Value](validationcategory/value/none.md)
  Indicates that the code is either adhoc signed or signed by an un-recognized certificate chain.
- [static let platform: ValidationCategory.Value](validationcategory/value/platform.md)
  Indicates that the code is signed by Apple or allowed by a loaded trustcache.
- [static let testflight: ValidationCategory.Value](validationcategory/value/testflight.md)
  Indicates that the code is signed by Apple’s TestFlight certificate
### Default Implementations
- [Equatable Implementations](validationcategory/value/equatable-implementations.md)
- [RawRepresentable Implementations](validationcategory/value/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/validationcategory/value)*