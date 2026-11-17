# containerIdentifier

**Framework**: PhotosUI  
**Kind**: property  
**Role**: Instance Property

The collection of items that can be shown. Default is `nil`.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
var containerIdentifier: String? { get set }
```

## Discussion

Setting `containerIdentifier` to `nil` means items in any collection can be shown. An identifier that doesn’t resolve is treated as `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phpickerconfiguration-swift.struct/containeridentifier)*