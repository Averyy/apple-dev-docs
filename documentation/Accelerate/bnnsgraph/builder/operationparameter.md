# BNNSGraph.Builder.OperationParameter

**Framework**: Accelerate  
**Kind**: protocol

A protocol that allows functions to accept either tensors or collections.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
protocol OperationParameter<Element>
```

## Topics

### Operators
- [static func * (Self, BNNSGraph.Builder.Tensor<Self.Element>) -> BNNSGraph.Builder.Tensor<Self.Element>](bnnsgraph/builder/operationparameter/*(_:_:)-386tk.md)
  Adds an element-wise multiplication operation to the current graph.
- [static func * (BNNSGraph.Builder.Tensor<Self.Element>, Self) -> BNNSGraph.Builder.Tensor<Self.Element>](bnnsgraph/builder/operationparameter/*(_:_:)-3h4np.md)
  Adds an element-wise multiplication operation to the current graph.
- [static func + (BNNSGraph.Builder.Tensor<Self.Element>, Self) -> BNNSGraph.Builder.Tensor<Self.Element>](bnnsgraph/builder/operationparameter/+(_:_:)-2u9f3.md)
  Adds an element-wise addition operation to the current graph.
- [static func + (Self, BNNSGraph.Builder.Tensor<Self.Element>) -> BNNSGraph.Builder.Tensor<Self.Element>](bnnsgraph/builder/operationparameter/+(_:_:)-8d4pt.md)
  Adds an element-wise addition operation to the current graph.
- [static func - (Self, BNNSGraph.Builder.Tensor<Self.Element>) -> BNNSGraph.Builder.Tensor<Self.Element>](bnnsgraph/builder/operationparameter/-(_:_:)-8vtfy.md)
  Adds an element-wise subtraction operation to the current graph.
- [static func - (BNNSGraph.Builder.Tensor<Self.Element>, Self) -> BNNSGraph.Builder.Tensor<Self.Element>](bnnsgraph/builder/operationparameter/-(_:_:)-9ywu4.md)
  Adds an element-wise subtraction operation to the current graph.
- [static func / (Self, BNNSGraph.Builder.Tensor<Self.Element>) -> BNNSGraph.Builder.Tensor<Self.Element>](bnnsgraph/builder/operationparameter/_(_:_:)-1ojod.md)
  Adds an element-wise division operation to the current graph.
- [static func / (BNNSGraph.Builder.Tensor<Self.Element>, Self) -> BNNSGraph.Builder.Tensor<Self.Element>](bnnsgraph/builder/operationparameter/_(_:_:)-78g8y.md)
  Adds an element-wise division operation to the current graph.
- [static func % (BNNSGraph.Builder.Tensor<Self.Element>, Self) -> BNNSGraph.Builder.Tensor<Self.Element>](bnnsgraph/builder/operationparameter/_(_:_:)-8fwxf.md)
  Adds an element-wise remainder of division operation to the current graph.
### Associated Types
- [associatedtype Element : BNNSScalar](bnnsgraph/builder/operationparameter/element.md)
### Instance Methods
- [func graphBuilderTensor(BNNSGraph.Builder) -> BNNSGraph.Builder.Tensor<Self.Element>](bnnsgraph/builder/operationparameter/graphbuildertensor(_:).md)
  Returns a tensor for the specified BNNS Graph builder.

## Relationships

### Conforming Types
- [BNNSGraph.Builder.Tensor](bnnsgraph/builder/tensor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/operationparameter)*