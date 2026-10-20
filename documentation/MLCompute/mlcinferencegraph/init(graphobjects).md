# init(graphObjects:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates an inference graph with the layers from the graph objects you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
convenience init(graphObjects: [MLCGraph])
```

```objc
+ (instancetype) graphWithGraphObjects:(NSArray<MLCGraph *> *) graphObjects;
```

## Parameters

- `graphObjects`: The graph objects whose layers you add to the inference graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcinferencegraph/init(graphobjects:))*