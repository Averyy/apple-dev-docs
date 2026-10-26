# imageSize(for:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Returns the preferred image size for the specified response object.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func imageSize(for response: INIntentResponse) -> CGSize
```

```objc
+ (CGSize) imageSizeForIntentResponse:(INIntentResponse *) response;
```

#### Return Value

The response object’s preferred image size.

#### Discussion

If a response object includes an image, use this method to get its preferred size and then create an image of that size.

## Parameters

- `response`: The response object that uses the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inimage/imagesize(for:))*