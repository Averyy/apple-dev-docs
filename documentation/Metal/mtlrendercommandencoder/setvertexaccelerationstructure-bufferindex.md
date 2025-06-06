# setVertexAccelerationStructure(_:bufferIndex:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Assigns an acceleration structure to an entry in the vertex shader argument table.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func setVertexAccelerationStructure(_ accelerationStructure: (any MTLAccelerationStructure)?, bufferIndex: Int)
```

#### Discussion

By default, the acceleration structure at each index is `nil`.

## Parameters

- `accelerationStructure`: An   instance the command assigns to an entry in the vertex shader argument table for acceleration structures.
- `bufferIndex`: An integer that represents the entry in the vertex shader argument table for acceleration structures that stores a record of  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setvertexaccelerationstructure(_:bufferindex:))*