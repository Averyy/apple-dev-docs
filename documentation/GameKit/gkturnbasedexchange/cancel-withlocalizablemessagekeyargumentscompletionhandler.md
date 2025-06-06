# cancel(withLocalizableMessageKey:arguments:completionHandler:)

**Framework**: GameKit  
**Kind**: method

Cancels an exchange request.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func cancel(withLocalizableMessageKey key: String, arguments: [String]) async throws
```

## Mentions

- [Exchanging data between players in turn-based games](exchanging-data-between-players-in-turn-based-games.md)

#### Discussion

You can cancel both an active and completed exchange request.

If your game isn’t running or is in the background on recipient devices, a notification containing the localized message you provide appears. When the participant taps or clicks the notification, GameKit launches or brings the game to the foreground and then invokes the [`player(_:receivedExchangeCancellation:for:)`](gkturnbasedeventlistener/player(_:receivedexchangecancellation:for:).md) protocol method.

## Parameters

- `key`: The identifier for looking up the translated cancel message in the default   file. If you use a formatted string with specifiers, provide the arguments.
- `arguments`: A list of arguments to substitute into the localized string if it’s formatted and contains specifiers.
- `completionHandler`: The block receives the following parameter:


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/cancel(withlocalizablemessagekey:arguments:completionhandler:))*