# loadImage(completionHandler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Loads the image set on the challenge definition, which may be `nil` if none was set.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
func loadImage(completionHandler: @escaping @Sendable (UIImage?, (any Error)?) -> Void)
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
var image: UIImage? { get async throws }
```

*macOS*

```swift
func loadImage(completionHandler: @escaping @Sendable (NSImage?, (any Error)?) -> Void)
```

*macOS*

```swift
var image: NSImage? { get async throws }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
- (void) loadImageWithCompletionHandler:(void (^)(UIImage *image, NSError *error)) completionHandler;
```

*macOS*

```objc
- (void) loadImageWithCompletionHandler:(void (^)(NSImage *image, NSError *error)) completionHandler;
```

## See Also

### Getting the display properties and image
- [var title: String](./title.md)
  A short title for the challenge definition.
- [var details: String?](./details.md)
  A more detailed description of the challenge definition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkchallengedefinition/loadimage(completionhandler:))*