# SecTransformCopyExternalRepresentation(_:)

**Framework**: Security  
**Kind**: func

Creates a dictionary that contains enough information to be able to recreate a transform.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func SecTransformCopyExternalRepresentation(_ transformRef: SecTransform) -> CFDictionary
```

#### Discussion

This function returns a CFDictionaryRef that contains sufficient information to be able to recreate this transform. You can pass this CFDictionaryRef to SecTransformCreateFromExternalRepresentation to be able to recreate the transform. The dictionary can also be written out to disk using the techniques described here.

http://developer.apple.com/mac/library/documentation/CoreFoundation/Conceptual/CFPropertyLists/Articles/Saving.html

## Parameters

- `transformRef`: The transformRef to be externalized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransformcopyexternalrepresentation(_:))*