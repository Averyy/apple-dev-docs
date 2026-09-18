# PrivateCloudComputeLanguageModel.Error.NetworkFailure

**Framework**: Foundation Models  
**Kind**: struct

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
- [init(debugDescription: String)](privatecloudcomputelanguagemodel/error/networkfailure/init(debugdescription:).md)
  Creates a network failure with the debug description you specify.
### Getting the error description
- [var debugDescription: String](privatecloudcomputelanguagemodel/error/networkfailure/debugdescription.md)
  A debug description of the network failure.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [case networkFailure(PrivateCloudComputeLanguageModel.Error.NetworkFailure)](privatecloudcomputelanguagemodel/error/networkfailure(_:).md)
  An error that occurs when a network is available, but PCC is inaccessible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/privatecloudcomputelanguagemodel/error/networkfailure)*