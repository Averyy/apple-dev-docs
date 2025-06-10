# groupID

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
var groupID: Int { get }
```

#### Discussion

A number associated with object groups (e.g., face and body) that is unique for each physical object (e.g., a person whom the face and body belong to).

The value of this property is an NSInteger indicating the unique identifier to combine objects (for instance, face and body) into groups (a physical person). A human body and face for the same person will have the same group ID. It is set to -1 when it’s invalid or not available. When it’s set to a value of >=0, it is unique across all object groups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataobject/groupid)*