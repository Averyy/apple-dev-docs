# init(point:)

**Framework**: GameplayKit  
**Kind**: init  
**Role**: Initializer

Initializes a graph node with the specified point.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
init(point: vector_float3)
```

```objc
- (instancetype) initWithPoint:(vector_float3) point;
```

## Return Value

A new graph node representing the specified point.

## Discussion

For more information, see [GameplayKit Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Parameters

- `point`: The position for the node in continuous 3D space.

## See Also

### Creating a Graph Node
- [class func node(withPoint: vector_float3) -> Self](./node%28withpoint%29.md)
  Creates a graph node with the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgraphnode3d/init(point:))*