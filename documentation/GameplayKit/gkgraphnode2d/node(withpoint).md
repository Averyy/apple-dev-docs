# node(withPoint:)

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Type Method

Creates a graph node with the specified point.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func node(withPoint point: vector_float2) -> Self
```

```objc
+ (instancetype) nodeWithPoint:(vector_float2) point;
```

## Return Value

A new graph node representing the specified point.

## Parameters

- `point`: The position for the node in continuous 2D space.

## See Also

### Creating a Graph Node
- [init(point: vector_float2)](./init%28point%29.md)
  Initializes a graph node with the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgraphnode2d/node(withpoint:))*