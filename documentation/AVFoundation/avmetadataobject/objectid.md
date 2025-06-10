# objectID

**Framework**: AVFoundation  
**Kind**: property

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)

## Declaration

```swift
var objectID: Int { get }
```

#### Discussion

A unique identifier for each detected object type (face, body, hands, heads and salient objects).

Defaults to a value of -1 when it is invalid or not available. When a new object enters the picture, it is assigned a new unique identifier. objectIDs are not re-used as objects leave the picture and new ones enter. Objects that leave the picture then re-enter are assigned a new objectID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataobject/objectid)*