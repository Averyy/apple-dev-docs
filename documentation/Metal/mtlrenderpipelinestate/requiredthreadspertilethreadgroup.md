# requiredThreadsPerTileThreadgroup

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var requiredThreadsPerTileThreadgroup: MTLSize { get }
```

```objc
@property (readonly) MTLSize requiredThreadsPerTileThreadgroup;
```

## Discussion

The required size of every tile shader threadgroup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinestate/requiredthreadspertilethreadgroup)*