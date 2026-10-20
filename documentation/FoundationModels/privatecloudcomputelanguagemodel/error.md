# PrivateCloudComputeLanguageModel.Error

**Framework**: Foundation Models  
**Kind**: enum  
**Role**: Enumeration

Errors that may occur when using Private Cloud Compute.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
enum Error
```

## Topics

### Quota usage error
- [case quotaLimitReached(PrivateCloudComputeLanguageModel.Error.QuotaLimitReached)](./error/quotalimitreached%28_%29.md)
  The allotted usage quota has been reached.
- [PrivateCloudComputeLanguageModel.Error.QuotaLimitReached](./error/quotalimitreached.md)
  Information about reaching a usage limit.
### Network failure error
- [case networkFailure(PrivateCloudComputeLanguageModel.Error.NetworkFailure)](./error/networkfailure%28_%29.md)
  An error that occurs when a network is available, but PCC is inaccessible.
- [PrivateCloudComputeLanguageModel.Error.NetworkFailure](./error/networkfailure.md)
  Information about a network problem that prevented a request from completing.
### Service unavailable error
- [case serviceUnavailable(PrivateCloudComputeLanguageModel.Error.ServiceUnavailable)](./error/serviceunavailable%28_%29.md)
  Services are unavailable.
- [PrivateCloudComputeLanguageModel.Error.ServiceUnavailable](./error/serviceunavailable.md)
  Information about the model service being unable to handle a request.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [Error](../../Swift/error.md)
- [Escapable](../../Swift/escapable.md)
- [LocalizedError](../../Foundation/localizederror.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/privatecloudcomputelanguagemodel/error)*