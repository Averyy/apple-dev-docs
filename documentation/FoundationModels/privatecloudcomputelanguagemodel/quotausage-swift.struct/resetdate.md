# resetDate

**Framework**: Foundation Models  
**Kind**: property

The date at which the quota will refresh.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var resetDate: Date?
```

## Mentions

- [Adding server-side intelligence with Private Cloud Compute](adding-server-side-intelligence-with-private-cloud-compute.md)

#### Discussion

A `nil` value indicates that the model provider has not reported a reset time. This may be because the provider’s limit does not refresh on a fixed schedule, or because the provider does not expose this information.

## See Also

- [var status: PrivateCloudComputeLanguageModel.QuotaUsage.Status](privatecloudcomputelanguagemodel/quotausage-swift.struct/status-swift.property.md)
  The current quota status.
- [PrivateCloudComputeLanguageModel.QuotaUsage.Status](privatecloudcomputelanguagemodel/quotausage-swift.struct/status-swift.enum.md)
  The quota status of a language model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/privatecloudcomputelanguagemodel/quotausage-swift.struct/resetdate)*