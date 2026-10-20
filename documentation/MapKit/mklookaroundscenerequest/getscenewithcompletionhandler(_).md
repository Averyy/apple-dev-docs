# getSceneWithCompletionHandler(_:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Requests a LookAround scene and calls the specified completion handler.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func getSceneWithCompletionHandler(_ completionHandler: @escaping @MainActor @Sendable (MKLookAroundScene?, (any Error)?) -> Void)
```

```swift
var scene: MKLookAroundScene? { get async throws }
```

```objc
- (void) getSceneWithCompletionHandler:(void (^)(MKLookAroundScene *, NSError *)) completionHandler;
```

## Parameters

- `completionHandler`: A completion handler the framework calls when the scene request completes to indicate the success or failure of the request.

## See Also

### Starting and stopping scene requests
- [func cancel()](./cancel%28%29.md)
  Cancels the pending scene request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklookaroundscenerequest/getscenewithcompletionhandler(_:))*