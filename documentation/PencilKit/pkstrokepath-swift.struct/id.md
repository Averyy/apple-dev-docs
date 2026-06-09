# id

**Framework**: PencilKit  
**Kind**: property

The unique identity of the stroke path.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var id: UUID { get }
```

#### Discussion

> ⚠️ **Warning**: Using multiple stroke paths with identical IDs but different control points will result in undefined rendering behavior. Ensure each stroke path has a unique identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokepath-swift.struct/id)*