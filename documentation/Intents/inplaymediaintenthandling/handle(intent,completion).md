# handle(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Handles the media playback request.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func handle(intent: INPlayMediaIntent, completion: @escaping @Sendable (INPlayMediaIntentResponse) -> Void)
```

```swift
func handle(intent: INPlayMediaIntent) async -> INPlayMediaIntentResponse
```

```objc
- (void) handlePlayMedia:(INPlayMediaIntent *) intent completion:(void (^)(INPlayMediaIntentResponse *response)) completion;
```

#### Discussion

Because the lifespan for an Intents app extension is short, the [`INPlayMediaIntent`](../inplaymediaintent.md) handler tells the main app to start the media playback. For audio content, respond with the [`INPlayMediaIntentResponseCode.handleInApp`](../inplaymediaintentresponsecode/handleinapp.md) response code. This code tells the system to launch the main app in the background and call [`application(_:handle:completionHandler:)`](../../UIKit/uiapplicationdelegate/application%28_,handle,completionhandler%29.md) on the [`UIApplicationDelegate`](../../UIKit/uiapplicationdelegate.md) object. Your app should begin the audio playback in this app delegate method.

The listing below tells the app to play the requested media in the background.

```swift
public func handle(intent: INPlayMediaIntent, completion: @escaping (INPlayMediaIntentResponse) -> Void) {
    let response = INPlayMediaIntentResponse(code: .handleInApp, userActivity: nil)
    completion(response)
}
```

For video content, respond with [`INPlayMediaIntentResponseCode.continueInApp`](../inplaymediaintentresponsecode/continueinapp.md). This code instructs the system to launch your app in the foreground and call [`application(_:continue:restorationHandler:)`](../../UIKit/uiapplicationdelegate/application%28_,continue,restorationhandler%29.md) on the [`UIApplicationDelegate`](../../UIKit/uiapplicationdelegate.md) object. Your app should start the video playback in this app delegate method.

The listing below tells the app to play the requested media in the foreground.

```swift
public func handle(intent: INPlayMediaIntent, completion: @escaping (INPlayMediaIntentResponse) -> Void) {
    let response = INPlayMediaIntentResponse(code: .continueInApp, userActivity: nil)
    completion(response)
}

```

## Parameters

- `intent`: The [`INPlayMediaIntent`](../inplaymediaintent.md) object that contains details about the user’s request. The Intents app extension confirms the information in this intent before the system calls the [`handle(intent:completion:)`](./handle%28intent,completion%29.md) method.
- `completion`: The handler block to execute with your response. You must execute this handler while implementing this method. This handler has no return value and takes the following parameter:

  - **`response`**: The [`INPlayMediaIntentResponse`](../inplaymediaintentresponse.md) object you create that reports the status of the request. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inplaymediaintenthandling/handle(intent:completion:))*