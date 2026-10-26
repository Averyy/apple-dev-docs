# INSearchForPhotosIntentResponseCode

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the status of the response.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
enum INSearchForPhotosIntentResponseCode
```

```c
enum INSearchForPhotosIntentResponseCode : NSInteger;
```

## Topics

### Constants
- [INSearchForPhotosIntentResponseCode.unspecified](./insearchforphotosintentresponsecode/unspecified.md)
  Your app doesn’t provide a specific status.
- [INSearchForPhotosIntentResponseCode.ready](./insearchforphotosintentresponsecode/ready.md)
  You’re ready to handle the intent.
- [INSearchForPhotosIntentResponseCode.continueInApp](./insearchforphotosintentresponsecode/continueinapp.md)
  Your extension is ready to transfer control to the app in order to display the search results.
- [INSearchForPhotosIntentResponseCode.failure](./insearchforphotosintentresponsecode/failure.md)
  You were unable to perform the search.
- [INSearchForPhotosIntentResponseCode.failureRequiringAppLaunch](./insearchforphotosintentresponsecode/failurerequiringapplaunch.md)
  The user must launch your app to search their photos.
- [INSearchForPhotosIntentResponseCode.failureAppConfigurationRequired](./insearchforphotosintentresponsecode/failureappconfigurationrequired.md)
  The user must perform additional configuration steps before searching for photos is possible.
### Initializers
- [init?(rawValue: Int)](./insearchforphotosintentresponsecode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the Response Code
- [var code: INSearchForPhotosIntentResponseCode](./insearchforphotosintentresponse/code.md)
  The code indicating whether you successfully handled the intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforphotosintentresponsecode)*