# default()

**Framework**: Photos  
**Kind**: method  
**Role**: Type Method

Returns the shared asset resource manager object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func `default`() -> PHAssetResourceManager
```

```objc
+ (PHAssetResourceManager *) defaultManager;
```

## Return Value

The asset resource manager.

## Discussion

This method always returns the same asset resource manager object, which is shared for all uses in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresourcemanager/default())*