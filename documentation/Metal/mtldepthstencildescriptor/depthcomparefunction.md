# depthCompareFunction

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The comparison that is performed between a fragment’s depth value and the depth value in the attachment, which determines whether to discard the fragment.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var depthCompareFunction: MTLCompareFunction { get set }
```

```objc
@property (nonatomic) MTLCompareFunction depthCompareFunction;
```

## Discussion

The default value is [`MTLCompareFunction.always`](../mtlcomparefunction/always.md), which indicates that the depth test always passes and the fragment remains a candidate to replace the data at the specified location. For more information on possible values, see [`MTLCompareFunction`](../mtlcomparefunction.md).

## See Also

### Related Documentation
- [Metal Shading Language Guide](https://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)
### Specifying depth operations
- [var isDepthWriteEnabled: Bool](./isdepthwriteenabled.md)
  A Boolean value that indicates whether depth values can be written to the depth attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldepthstencildescriptor/depthcomparefunction)*