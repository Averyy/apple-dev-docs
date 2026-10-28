# es_cs_validation_category_t

**Framework**: Endpoint Security  
**Kind**: struct  
**Role**: Structure

es_cs_validation_category

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
struct es_cs_validation_category_t
```

```c
typedef enum { ... } es_cs_validation_category_t;
```

## Overview

Indicates the code signature validation policy that was applied to a binary

## Topics

### Initializers
- [init(UInt32)](./es_cs_validation_category_t/init%28_%29.md)
- [init(rawValue: UInt32)](./es_cs_validation_category_t/init%28rawvalue%29.md)
### Instance Properties
- [var rawValue: UInt32](./es_cs_validation_category_t/rawvalue.md)
### Enumeration Cases
- [ES_CS_VALIDATION_CATEGORY_APP_STORE](./es_cs_validation_category_app_store.md)
- [ES_CS_VALIDATION_CATEGORY_DEVELOPER_ID](./es_cs_validation_category_developer_id.md)
- [ES_CS_VALIDATION_CATEGORY_DEVELOPMENT](./es_cs_validation_category_development.md)
- [ES_CS_VALIDATION_CATEGORY_ENTERPRISE](./es_cs_validation_category_enterprise.md)
- [ES_CS_VALIDATION_CATEGORY_INVALID](./es_cs_validation_category_invalid.md)
- [ES_CS_VALIDATION_CATEGORY_LOCAL_SIGNING](./es_cs_validation_category_local_signing.md)
- [ES_CS_VALIDATION_CATEGORY_NONE](./es_cs_validation_category_none.md)
- [ES_CS_VALIDATION_CATEGORY_OOPJIT](./es_cs_validation_category_oopjit.md)
- [ES_CS_VALIDATION_CATEGORY_PLATFORM](./es_cs_validation_category_platform.md)
- [ES_CS_VALIDATION_CATEGORY_ROSETTA](./es_cs_validation_category_rosetta.md)
- [ES_CS_VALIDATION_CATEGORY_TESTFLIGHT](./es_cs_validation_category_testflight.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_cs_validation_category_t)*