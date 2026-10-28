# confirm(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Confirms the details of the media playback request.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
optional func confirm(intent: INPlayMediaIntent, completion: @escaping @Sendable (INPlayMediaIntentResponse) -> Void)
```

```swift
optional func confirm(intent: INPlayMediaIntent) async -> INPlayMediaIntentResponse
```

```objc
- (void) confirmPlayMedia:(INPlayMediaIntent *) intent completion:(void (^)(INPlayMediaIntentResponse *response)) completion;
```

## Discussion

Implement this method to determine whether your app can play the requested media. If it can, respond with the [`INPlayMediaIntentResponseCode.ready`](../inplaymediaintentresponsecode/ready.md) response code. Include the [`nowPlayingInfo`](../inplaymediaintentresponse/nowplayinginfo.md) dictionary in the response, so the system can display information such as title, artist, and artwork, about the media.

When your Intents app extension doesn’t provide this method, the system assumes your app can play the media.

If your app can’t play the media, respond with the appropriate failure code.

## Parameters

- `intent`: The [`INPlayMediaIntent`](../inplaymediaintent.md) object that contains details about the user’s request.
- `completion`: The handler block to execute with your response. You must execute this handler while implementing this method. This handler has no return value and takes the following parameter:

  - **`response`**: The [`INPlayMediaIntentResponse`](../inplaymediaintentresponse.md) object that contains the response code which determines whether your app can play back the media content. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inplaymediaintenthandling/confirm(intent:completion:))*