# es_tcc_identity_type_t

**Framework**: Endpoint Security  
**Kind**: struct  
**Role**: Structure

es_tcc_identity_type_t

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
struct es_tcc_identity_type_t
```

```c
typedef enum { ... } es_tcc_identity_type_t;
```

#### Overview

Represent the identity type of an application which has access to a TCC service.

## Topics

### Initializers
- [init(UInt32)](./es_tcc_identity_type_t/init%28_%29.md)
- [init(rawValue: UInt32)](./es_tcc_identity_type_t/init%28rawvalue%29.md)
### Instance Properties
- [var rawValue: UInt32](./es_tcc_identity_type_t/rawvalue.md)
### Enumeration Cases
- [ES_TCC_IDENTITY_TYPE_BUNDLE_ID](./es_tcc_identity_type_bundle_id.md)
- [ES_TCC_IDENTITY_TYPE_EXECUTABLE_PATH](./es_tcc_identity_type_executable_path.md)
- [ES_TCC_IDENTITY_TYPE_FILE_PROVIDER_DOMAIN_ID](./es_tcc_identity_type_file_provider_domain_id.md)
- [ES_TCC_IDENTITY_TYPE_POLICY_ID](./es_tcc_identity_type_policy_id.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_tcc_identity_type_t)*