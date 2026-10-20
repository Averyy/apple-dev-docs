# PrivateCloudComputeLanguageModel.Error.NetworkFailure

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

Information about a network problem that prevented a request from completing.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct NetworkFailure
```

## Topics

### Creating a network failure error
- [init(debugDescription: String)](./networkfailure/init%28debugdescription%29.md)
  Creates a network failure with the debug description you specify.
### Getting the error description
- [var debugDescription: String](./networkfailure/debugdescription.md)
  A debug description of the network failure.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Network failure error
- [case networkFailure(PrivateCloudComputeLanguageModel.Error.NetworkFailure)](./networkfailure%28_%29.md)
  An error that occurs when a network is available, but PCC is inaccessible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/privatecloudcomputelanguagemodel/error/networkfailure)*