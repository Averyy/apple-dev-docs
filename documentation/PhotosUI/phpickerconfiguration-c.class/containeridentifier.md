# containerIdentifier

**Framework**: PhotosUI  
**Kind**: property  
**Role**: Instance Property

The collection of items that can be shown. Default is \c nil.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```objc
@property (nonatomic, copy, nullable) NSString * containerIdentifier;
```

## Discussion

Setting \c containerIdentifier to \c nil means items in any collection can be shown. An identifier that doesn’t resolve is treated as \c nil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phpickerconfiguration-c.class/containeridentifier)*