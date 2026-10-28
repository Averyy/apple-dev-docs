# constituentFileURLs

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The list of file URLs that collectively represent the media asset.

**Availability**:
- macOS 27.0+

## Declaration

```objc
@property (nonatomic, readonly) NSArray<NSURL *> * constituentFileURLs;
```

## Discussion

The list of file URLs that constitute the asset are returned only for QuickTime reference movies, or if the MediaExtension format reader implements this property [MEFileInfo setConstituentFileNames:].


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/constituentfileurls)*