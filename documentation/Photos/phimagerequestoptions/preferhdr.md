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
@property (nonatomic, assign) BOOL preferHDR;
```

## Discussion

When set to `YES`, the image manager will attempt to provide HDR image data if the asset contains HDR content. Defaults to `NO`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phimagerequestoptions/preferhdr)*