# PrivateCloudComputeLanguageModel.Error

**Framework**: Foundation Models  
**Kind**: enum

Errors that may occur when using Private Cloud Compute.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
enum Error
```

## Topics

### Quota usage error
- [case quotaLimitReached(PrivateCloudComputeLanguageModel.Error.QuotaLimitReached)](privatecloudcomputelanguagemodel/error/quotalimitreached(_:).md)
  The allotted usage quota has been reached.
- [PrivateCloudComputeLanguageModel.Error.QuotaLimitReached](privatecloudcomputelanguagemodel/error/quotalimitreached.md)
  Information about reaching a usage limit.
### Network failure error
- [case networkFailure(PrivateCloudComputeLanguageModel.Error.NetworkFailure)](privatecloudcomputelanguagemodel/error/networkfailure(_:).md)
  An error that occurs when a network is available, but PCC is inaccessible.
- [PrivateCloudComputeLanguageModel.Error.NetworkFailure](privatecloudcomputelanguagemodel/error/networkfailure.md)
### Service unavailable error
- [case serviceUnavailable(PrivateCloudComputeLanguageModel.Error.ServiceUnavailable)](privatecloudcomputelanguagemodel/error/serviceunavailable(_:).md)
  Services are unavailable.
- [PrivateCloudComputeLanguageModel.Error.ServiceUnavailable](privatecloudcomputelanguagemodel/error/serviceunavailable.md)

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [Error](../swift/error.md)
- [Escapable](../swift/escapable.md)
- [LocalizedError](../foundation/localizederror.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/privatecloudcomputelanguagemodel/error)*