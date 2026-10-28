# shared()

**Framework**: Photos  
**Kind**: method  
**Role**: Type Method

Retrieves the shared photo library object.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func shared() -> PHPhotoLibrary
```

```objc
+ (PHPhotoLibrary *) sharedPhotoLibrary;
```

## Return Value

The singleton photo library object.

## Discussion

You may use the shared photo library object from any thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phphotolibrary/shared())*