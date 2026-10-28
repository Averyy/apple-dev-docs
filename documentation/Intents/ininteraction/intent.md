# intent

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The intent object that describes the user’s request.

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
var intent: INIntent { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) INIntent * intent;
```

*macOS*

```objc
@property (atomic, copy, readonly) INIntent * intent;
```

## Discussion

This property is set at initialization time and cannot be changed later. Use the object in this property to get information about the user’s initial request.

## See Also

### Getting the Intent and Response
- [var intentResponse: INIntentResponse?](./intentresponse.md)
  The response object that your app created in response to the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ininteraction/intent)*