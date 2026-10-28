# init(mediaDestinationResolutionResult:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates an object whose resolution involves successfully adding a media item to a particular destination.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(mediaDestinationResolutionResult: INMediaDestinationResolutionResult)
```

```objc
- (instancetype) initWithMediaDestinationResolutionResult:(INMediaDestinationResolutionResult *) mediaDestinationResolutionResult;
```

## Return Value

A new [`INAddMediaMediaDestinationResolutionResult`](../inaddmediamediadestinationresolutionresult.md) object.

## Discussion

Use this method to create a result object when you’re able to add a media item to a particular destination.

## Parameters

- `mediaDestinationResolutionResult`: The value that resolves the requested parameter of the intent. This value may be different than the one specified in the intent object.

## See Also

### Creating a Resolution Result
- [class func unsupported(forReason: INAddMediaMediaDestinationUnsupportedReason) -> Self](./unsupported%28forreason%29.md)
  Creates an object whose resolution requires the user to confirm the media destination.
- [enum INAddMediaMediaDestinationUnsupportedReason](../inaddmediamediadestinationunsupportedreason.md)
  Reasons describing why the destination is not supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddmediamediadestinationresolutionresult/init(mediadestinationresolutionresult:))*