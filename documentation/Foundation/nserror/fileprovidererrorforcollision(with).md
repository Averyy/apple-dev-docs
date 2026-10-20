# fileProviderErrorForCollision(with:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns a properly formatted error object with a `NSFileProviderItemCollisionError` error code.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class func fileProviderErrorForCollision(with existingItem: NSFileProviderItem) -> Self
```

```objc
+ (instancetype) fileProviderErrorForCollisionWithItem:(NSFileProviderItem) existingItem;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nserror/fileprovidererrorforcollision(with:))*