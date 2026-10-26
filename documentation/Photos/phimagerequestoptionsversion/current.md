# PHImageRequestOptionsVersion.current

**Framework**: Photos  
**Kind**: case  
**Role**: Case

Request the most recent version of the image asset (the one that reflects all edits).

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case current
```

```c
PHImageRequestOptionsVersionCurrent
```

#### Discussion

The resulting image is the rendered output from all previously made adjustments.

## See Also

### Constants
- [PHImageRequestOptionsVersion.unadjusted](./unadjusted.md)
  Request a version of the image asset without adjustments.
- [PHImageRequestOptionsVersion.original](./original.md)
  Request the original, highest-fidelity version of the image asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phimagerequestoptionsversion/current)*