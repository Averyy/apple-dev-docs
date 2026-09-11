# renderGroupID

**Framework**: PencilKit  
**Kind**: property

A UUID that groups strokes for wet-ink compositing with compatible inks such as marker.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var renderGroupID: UUID? { get }
```

#### Discussion

Set this to the same value for a run of strokes to render them as if drawn while the previous stroke with the same ink was still wet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokereference/rendergroupid)*