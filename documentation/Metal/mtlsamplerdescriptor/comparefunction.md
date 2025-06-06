# compareFunction

**Framework**: Metal  
**Kind**: property

The sampler comparison function used when performing a sample compare operation on a depth texture.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var compareFunction: MTLCompareFunction { get set }
```

#### Discussion

The default value is [`MTLCompareFunction.never`](mtlcomparefunction/never.md).

The [`MTLFeatureSet.iOS_GPUFamily3_v1`](mtlfeatureset/ios_gpufamily3_v1.md) and [`MTLFeatureSet.iOS_GPUFamily1_v1`](mtlfeatureset/ios_gpufamily1_v1.md) feature sets allow you to define a framework-side sampler comparison function for a [`MTLSamplerState`](mtlsamplerstate.md) object. All feature sets support shader-side sampler comparison functions, as described in the [`Metal Shading Language Specification`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf).

## See Also

- [enum MTLCompareFunction](mtlcomparefunction.md)
  Options used to specify how a sample compare operation should be performed on a depth texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsamplerdescriptor/comparefunction)*