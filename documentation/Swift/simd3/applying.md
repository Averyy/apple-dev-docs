# applying(_:)

**Framework**: Swift  
**Kind**: method

Returns a simd vector that’s transformed by the specified projective transform.

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
func applying(_ transform: ProjectiveTransform3DFloat) -> simd_float3
```

#### Discussion

- Returns The transformed ray.

This function applies the transform to the simd vector.

## Parameters

- `transform`: The projective transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/simd3/applying(_:))*