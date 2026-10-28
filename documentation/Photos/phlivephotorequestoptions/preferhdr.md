# preferHDR

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

Request HDR image data if available (such as PQ/HLG formats).

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var preferHDR: Bool { get set }
```

```objc
@property (nonatomic) BOOL preferHDR;
```

## Discussion

Off by default. For best results, only enable this when you intend to display an HDR experience in `PHLivePhotoView` — for example, when the view’s `preferredImageDynamicRange` is greater than standard (SDR). Defaults to `NO`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phlivephotorequestoptions/preferhdr)*