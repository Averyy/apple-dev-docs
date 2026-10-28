# PHImageRequestOptionsVersion.original

**Framework**: Photos  
**Kind**: case  
**Role**: Case

Request the original, highest-fidelity version of the image asset.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case original
```

```c
PHImageRequestOptionsVersionOriginal
```

## Discussion

The resulting image is originally captured or imported version of the asset, regardless of any edits made.

If the image asset contains data in multiple formats, the resulting image data uses the highest quality format. For example, for an asset containing both RAW and JPEG data, Photos returns the RAW data.

## See Also

### Constants
- [PHImageRequestOptionsVersion.current](./current.md)
  Request the most recent version of the image asset (the one that reflects all edits).
- [PHImageRequestOptionsVersion.unadjusted](./unadjusted.md)
  Request a version of the image asset without adjustments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phimagerequestoptionsversion/original)*