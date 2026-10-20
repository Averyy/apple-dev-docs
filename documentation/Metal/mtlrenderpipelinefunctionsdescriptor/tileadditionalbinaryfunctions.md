# tileAdditionalBinaryFunctions

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The tile functions to add to the render pipeline.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var tileAdditionalBinaryFunctions: [any MTLFunction]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSArray<id<MTLFunction>> * tileAdditionalBinaryFunctions;
```

## See Also

### Configuring the descriptor’s functions
- [var vertexAdditionalBinaryFunctions: [any MTLFunction]?](./vertexadditionalbinaryfunctions.md)
  The vertex functions to add to the render pipeline.
- [var fragmentAdditionalBinaryFunctions: [any MTLFunction]?](./fragmentadditionalbinaryfunctions.md)
  The fragment functions to add to the render pipeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinefunctionsdescriptor/tileadditionalbinaryfunctions)*