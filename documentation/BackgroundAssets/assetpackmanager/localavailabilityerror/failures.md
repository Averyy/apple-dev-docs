# failures

**Framework**: Background Assets  
**Kind**: property

A dictionary that maps asset packs to errors describing why the system couldn’t ensure their local availability.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
let failures: [AssetPack : any Error]
```

## Mentions

- [Reducing download and storage demands with localized asset packs](reducing-download-and-storage-demands-with-localized-asset-packs.md)

## See Also

- [let successes: Set<AssetPack>](assetpackmanager/localavailabilityerror/successes.md)
  A set of asset packs for which the system successfully ensured local availability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanager/localavailabilityerror/failures)*