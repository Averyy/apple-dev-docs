# group

**Framework**: RealityKit  
**Kind**: property

The category this definition belongs to, or `nil` if uncategorized.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var group: String? { get }
```

#### Discussion

Group names are coarse categories such as `"math"`, `"texture"`, or `"geometric"`. For example, `ND_atan2_float` belongs to `"math"`.

Use this property to organize definitions into sections in a node picker or library browser UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraph/nodedefinition/group)*