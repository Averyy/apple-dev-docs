# init(point:)

**Framework**: GameplayKit  
**Kind**: init  
**Role**: Initializer

Initializes a graph node with the specified point.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(point: vector_float2)
```

```objc
- (instancetype) initWithPoint:(vector_float2) point;
```

#### Return Value

A new graph node representing the specified point.

#### Discussion

For more information, see [GameplayKit Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Parameters

- `point`: The position for the node in continuous 2D space.

## See Also

### Creating a Graph Node
- [class func node(withPoint: vector_float2) -> Self](./node%28withpoint%29.md)
  Creates a graph node with the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgraphnode2d/init(point:))*