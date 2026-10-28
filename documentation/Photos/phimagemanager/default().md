# default()

**Framework**: Photos  
**Kind**: method  
**Role**: Type Method

Returns the shared image manager object.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func `default`() -> PHImageManager
```

```objc
+ (PHImageManager *) defaultManager;
```

## Return Value

The image manager.

## Discussion

This method always returns the same image manager object, which is shared for all uses in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phimagemanager/default())*