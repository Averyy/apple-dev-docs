# isDepthWriteEnabled

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether depth values can be written to the depth attachment.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var isDepthWriteEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isDepthWriteEnabled) BOOL depthWriteEnabled;
```

#### Discussion

The default value is [`false`](../../Swift/false.md), which indicates the depth attachment is read-only.

## See Also

### Specifying depth operations
- [var depthCompareFunction: MTLCompareFunction](./depthcomparefunction.md)
  The comparison that is performed between a fragment’s depth value and the depth value in the attachment, which determines whether to discard the fragment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldepthstencildescriptor/isdepthwriteenabled)*