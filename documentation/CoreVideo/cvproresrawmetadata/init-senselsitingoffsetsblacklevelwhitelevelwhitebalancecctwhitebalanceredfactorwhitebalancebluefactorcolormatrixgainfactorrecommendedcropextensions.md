# init(senselSitingOffsets:blackLevel:whiteLevel:whiteBalanceCCT:whiteBalanceRedFactor:whiteBalanceBlueFactor:colorMatrix:gainFactor:recommendedCrop:extensions:)

**Framework**: Core Video  
**Kind**: init

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
init(senselSitingOffsets: CVSenselSitingOffsets = .zero, blackLevel: Int32, whiteLevel: Int32, whiteBalanceCCT: Float32? = nil, whiteBalanceRedFactor: Float32, whiteBalanceBlueFactor: Float32, colorMatrix: InlineArray<9, Float32>, gainFactor: Float32, recommendedCrop: CVProResRawMetadata.RecommendedCrop = .zero, extensions: Data? = nil)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvproresrawmetadata/init(senselsitingoffsets:blacklevel:whitelevel:whitebalancecct:whitebalanceredfactor:whitebalancebluefactor:colormatrix:gainfactor:recommendedcrop:extensions:))*