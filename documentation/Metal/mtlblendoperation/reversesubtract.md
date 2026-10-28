# MTLBlendOperation.reverseSubtract

**Framework**: Metal  
**Kind**: case  
**Role**: Case

Subtract a portion of the source values from a portion of the destination pixel values.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
case reverseSubtract
```

```c
MTLBlendOperationReverseSubtract
```

## Discussion

`RGB = Dest.rgb * DBF - Source.rgb * SBF`

`A = Dest.a * DBF - Source.a * SBF`

## See Also

### Blend operations
- [MTLBlendOperation.add](./add.md)
  Add portions of both source and destination pixel values.
- [MTLBlendOperation.subtract](./subtract.md)
  Subtract a portion of the destination pixel values from a portion of the source.
- [MTLBlendOperation.min](./min.md)
  Minimum of the source and destination pixel values.
- [MTLBlendOperation.max](./max.md)
  Maximum of the source and destination pixel values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblendoperation/reversesubtract)*