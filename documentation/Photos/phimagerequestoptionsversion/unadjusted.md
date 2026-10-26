# PHImageRequestOptionsVersion.unadjusted

**Framework**: Photos  
**Kind**: case  
**Role**: Case

Request a version of the image asset without adjustments.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case unadjusted
```

```c
PHImageRequestOptionsVersionUnadjusted
```

#### Discussion

If the asset has been edited, the resulting image reflects the state of the asset before any edits were performed.

## See Also

### Constants
- [PHImageRequestOptionsVersion.current](./current.md)
  Request the most recent version of the image asset (the one that reflects all edits).
- [PHImageRequestOptionsVersion.original](./original.md)
  Request the original, highest-fidelity version of the image asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phimagerequestoptionsversion/unadjusted)*