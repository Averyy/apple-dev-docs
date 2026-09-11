# failures

**Framework**: Background Assets  
**Kind**: property

A dictionary that maps asset packs to errors describing why the system couldn’t ensure their local availability.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

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