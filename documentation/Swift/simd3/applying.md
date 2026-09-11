# applying(_:)

**Framework**: Swift  
**Kind**: method

Returns a simd vector that’s transformed by the specified projective transform.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

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