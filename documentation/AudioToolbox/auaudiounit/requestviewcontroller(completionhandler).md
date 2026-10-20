# requestViewController(completionHandler:)

**Framework**: Audio Toolbox  
**Kind**: method  
**Role**: Instance Method

Requests an audio unit’s custom view controller.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
func requestViewController(completionHandler: @escaping @Sendable (UIViewController?) -> Void)
```

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
func requestViewController() async -> UIViewController?
```

*macOS*

```swift
func requestViewController(completionHandler: @escaping @Sendable (NSViewController?) -> Void)
```

*macOS*

```swift
func requestViewController() async -> NSViewController?
```

```objc
- (void) requestViewControllerWithCompletionHandler:(void (^)(AUViewControllerBase *viewController)) completionHandler;
```

## Mentions

- [Migrating Your Audio Unit Host to the AUv3 API](../migrating-your-audio-unit-host-to-the-auv3-api.md)

#### Discussion

The completion handler is called on a thread or dispatch queue internal to the audio unit’s implementation. If the audio unit does not implement a custom view controller, it returns `nil`. If it has a custom view controller, it instantiates the view controller and returns it. The custom view controller must be a subclass of [`AUViewController`](../../CoreAudioKit/auviewcontroller.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/requestviewcontroller(completionhandler:))*