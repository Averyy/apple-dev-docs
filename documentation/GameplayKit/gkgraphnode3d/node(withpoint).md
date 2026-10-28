# node(withPoint:)

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Type Method

Creates a graph node with the specified point.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func node(withPoint point: vector_float3) -> Self
```

```objc
+ (instancetype) nodeWithPoint:(vector_float3) point;
```

## Return Value

A new graph node representing the specified point.

## Parameters

- `point`: The position for the node in continuous 3D space.

## See Also

### Creating a Graph Node
- [init(point: vector_float3)](./init%28point%29.md)
  Initializes a graph node with the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgraphnode3d/node(withpoint:))*