# requestSiriAuthorization(_:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Requests authorization to use Siri services.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class func requestSiriAuthorization(_ handler: @escaping (INSiriAuthorizationStatus) -> Void)
```

```objc
+ (void) requestSiriAuthorization:(void (^)(INSiriAuthorizationStatus status)) handler;
```

## Mentions

- [Requesting Authorization to Use Siri](../../SiriKit/requesting-authorization-to-use-siri.md)

## Discussion

Call this method from your app to request authorization to integrate with Siri services. The first time you make this request, Siri prompts the user to grant or deny permission for your app to integrate with Siri. Subsequent calls to the method do not prompt the user again.

The block you provide in the `handler` parameter is executed asynchronously with the results of your authorization request.

## Parameters

- `handler`: The handler block to execute when the authorization status for your app is determined. This block has no return value and takes the following parameter:

  - **status**: The authorization status of your app. For a list of possible values, see [`INSiriAuthorizationStatus`](../insiriauthorizationstatus.md).

## See Also

### Managing the App’s Authorization
- [class func siriAuthorizationStatus() -> INSiriAuthorizationStatus](./siriauthorizationstatus%28%29.md)
  Returns the current authorization status of your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpreferences/requestsiriauthorization(_:))*