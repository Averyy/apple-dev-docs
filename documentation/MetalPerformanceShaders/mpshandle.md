# MPSHandle

**Framework**: Metal Performance Shaders  
**Kind**: protocol  
**Role**: Protocol

The protocol that provides resource identification.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
protocol MPSHandle : NSSecureCoding, NSObjectProtocol
```

```objc
@protocol MPSHandle <NSSecureCoding, NSObject>
```

## Topics

### Instance Methods
- [func label() -> String?](./mpshandle/label%28%29.md)

## Relationships

### Inherits From
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Neural Network Graphs
- [class MPSNNGraph](./mpsnngraph.md)
  An optimized representation of a graph of neural network image and filter nodes.
- [class MPSNNImageNode](./mpsnnimagenode.md)
  A placeholder node denoting the position of a neural network image in a graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpshandle)*