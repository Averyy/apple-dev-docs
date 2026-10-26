# fetchUIImage(completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Fetches the image and provides it to the specified completion handler.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func fetchUIImage(completion: @escaping @Sendable (UIImage?) -> Void)
```

```swift
func fetchUIImage() async -> UIImage?
```

```objc
- (void) fetchUIImageWithCompletion:(void (^)(UIImage *image)) completion;
```

#### Discussion

Use this method to fetch an instance of [`UIImage`](../../UIKit/uiimage.md) that contains the corresponding image data. Provide a completion handler; otherwise, calling this method does nothing. The handler executes on the same thread that invokes the method.

## Parameters

- `completion`: The completion handler that executes when the image is available. The handler has no return value and takes the following parameter:

  - **`image`**: A [`UIImage`](../../UIKit/uiimage.md) that contains the image data. If there’s an error, this parameter is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inimage/fetchuiimage(completion:))*