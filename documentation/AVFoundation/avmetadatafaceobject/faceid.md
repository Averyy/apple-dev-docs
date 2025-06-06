# faceID

**Framework**: AVFoundation  
**Kind**: property

The unique ID for this face metadata object.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 14.0+
- macOS 10.10+
- tvOS 9.0+

## Declaration

```swift
var faceID: Int { get }
```

#### Discussion

Each time a face enters the picture, it is assigned a new unique identifier, which you can use to reference the face in your code. Face IDs are not reused, and the same face leaving and entering the picture again is assigned a new identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadatafaceobject/faceid)*