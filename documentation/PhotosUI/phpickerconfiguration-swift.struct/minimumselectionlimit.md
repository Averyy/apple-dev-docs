# minimumSelectionLimit

**Framework**: PhotosUI  
**Kind**: property  
**Role**: Instance Property

The minimum number of assets that should be selected for some action. Default is `nil`.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
var minimumSelectionLimit: Int? { get set }
```

## Discussion

Setting `minimumSelectionLimit` to `nil` means 1 without preselection and 0 with preselection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phpickerconfiguration-swift.struct/minimumselectionlimit)*