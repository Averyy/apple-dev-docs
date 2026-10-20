# supportAddingBinaryFunctions

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether you can use the pipeline to create new pipelines by adding binary functions to its callable functions list.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var supportAddingBinaryFunctions: Bool { get set }
```

```objc
@property (nonatomic, readwrite) BOOL supportAddingBinaryFunctions;
```

## See Also

### Specifying precompiled shader binaries
- [var binaryArchives: [any MTLBinaryArchive]?](./binaryarchives.md)
  An array of binary archives to search for precompiled versions of the shader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltilerenderpipelinedescriptor/supportaddingbinaryfunctions)*