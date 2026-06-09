# validate(definition:nodeResourceMapping:skeletonResource:)

**Framework**: RealityKit  
**Kind**: method

Run the compiler and return all graph errors without producing a resource.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func validate(definition: Data, nodeResourceMapping: [Int : AnimationResource] = [:], skeletonResource: SkeletonResource) -> [String]
```

## See Also

- [convenience init(definition: Data, nodeResourceMapping: [Int : AnimationResource], skeletonResource: SkeletonResource) throws](animationgraphresource/init(definition:noderesourcemapping:skeletonresource:).md)
  Compile a new resource from data, throws on failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationgraphresource/validate(definition:noderesourcemapping:skeletonresource:))*