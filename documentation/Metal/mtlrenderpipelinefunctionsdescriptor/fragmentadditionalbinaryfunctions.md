# fragmentAdditionalBinaryFunctions

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The fragment functions to add to the render pipeline.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var fragmentAdditionalBinaryFunctions: [any MTLFunction]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSArray<id<MTLFunction>> * fragmentAdditionalBinaryFunctions;
```

## See Also

### Configuring the descriptor’s functions
- [var vertexAdditionalBinaryFunctions: [any MTLFunction]?](./vertexadditionalbinaryfunctions.md)
  The vertex functions to add to the render pipeline.
- [var tileAdditionalBinaryFunctions: [any MTLFunction]?](./tileadditionalbinaryfunctions.md)
  The tile functions to add to the render pipeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinefunctionsdescriptor/fragmentadditionalbinaryfunctions)*