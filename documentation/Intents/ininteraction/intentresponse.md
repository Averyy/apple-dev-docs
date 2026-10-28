# intentResponse

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The response object that your app created in response to the request.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
@NSCopying
var intentResponse: INIntentResponse? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INIntentResponse * intentResponse;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INIntentResponse * intentResponse;
```

## Discussion

This property is set at initialization time and cannot be changed later. Use this property to retrieve your app’s response to the specified [`intent`](./intent.md) object.

## See Also

### Getting the Intent and Response
- [var intent: INIntent](./intent.md)
  The intent object that describes the user’s request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ininteraction/intentresponse)*