# save(to:)

**Framework**: Immersive Media Support  
**Kind**: method  
**Role**: Instance Method

Generates an AIME file at the specified location.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.0+
- visionOS 26.4+

## Declaration

```swift
final func save(to aimeURL: URL) throws
```

## Parameters

- `aimeURL`: The destination URL with extension `.aime`.

## See Also

### Saving a venue descriptor data
- [var aimeData: Data?](./aimedata.md)
  Property holding the complete static metadata needed for the immersive media playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/venuedescriptor/save(to:))*