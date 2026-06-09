# constituentFileURLs

**Framework**: AVFoundation  
**Kind**: property

The list of file URLs used by the MediaExtension that constitute the asset. The list of file URLs that constitute the asset are returned only for QuickTime reference movies, or if the MediaExtension format reader implements this property [MEFileInfo setConstituentFileNames:].

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
static var constituentFileURLs: AVAsyncProperty<Root, [URL]> { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/constituentfileurls)*