# delegate

**Framework**: Background Assets  
**Kind**: property  
**Role**: Instance Property

An object that receives notifications about events that occur as an asset pack is downloaded.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
@property (weak, readwrite, nullable) id<BAManagedAssetPackDownloadDelegate> delegate;
```

## Mentions

- [Downloading Apple-hosted asset packs](../downloading-apple-hosted-asset-packs.md)

## See Also

### Tracking downloads
- [BAManagedAssetPackDownloadDelegate](../bamanagedassetpackdownloaddelegate.md)
  An object that handles status updates when downloading an asset pack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baassetpackmanager/delegate)*