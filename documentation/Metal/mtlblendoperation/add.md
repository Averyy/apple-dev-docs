# MTLBlendOperation.add

**Framework**: Metal  
**Kind**: case  
**Role**: Case

Add portions of both source and destination pixel values.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
case add
```

```c
MTLBlendOperationAdd
```

## Discussion

`RGB = Source.rgb * SBF + Dest.rgb * DBF`

`A = Source.a * SBF + Dest.a * DBF`

## See Also

### Blend operations
- [MTLBlendOperation.subtract](./subtract.md)
  Subtract a portion of the destination pixel values from a portion of the source.
- [MTLBlendOperation.reverseSubtract](./reversesubtract.md)
  Subtract a portion of the source values from a portion of the destination pixel values.
- [MTLBlendOperation.min](./min.md)
  Minimum of the source and destination pixel values.
- [MTLBlendOperation.max](./max.md)
  Maximum of the source and destination pixel values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblendoperation/add)*