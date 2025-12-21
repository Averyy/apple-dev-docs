# corners(in:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Resolved corners given a size. If the corner style of a shape is size-dependent, read the provided size and return values accordingly. This function could be called with a nil size when the size hasn’t been determined. In that case, return the best approximated value. For example, for a capsule shape, its corner radius is determined by the size. If size is not available, return `.fixed(.infinity)` to indicate that the corner should be as round as it could be.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func corners(in size: CGSize?) -> Self.Corners?
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/roundedrectangularshape/corners(in:))*