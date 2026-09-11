# resetDate

**Framework**: Foundation Models  
**Kind**: property

The date at which the quota refreshes.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

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