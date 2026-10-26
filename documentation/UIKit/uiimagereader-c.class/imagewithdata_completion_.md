# imageWithData:completion:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asynchronously generate an image from the given data. If an image could not be generated, the completion will be called with nil.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```objc
- (void) imageWithData:(NSData *) data completion:(void (^)(UIImage *)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagereader-c.class/imagewithdata:completion:)*