# renderGroupID

**Framework**: PencilKit  
**Kind**: property

A UUID that groups strokes for wet-ink compositing with compatible inks such as marker.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var renderGroupID: UUID? { get }
```

#### Discussion

Set this to the same value for a run of strokes to render them as if drawn while the previous stroke with the same ink was still wet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokereference/rendergroupid)*