# peopleInPhotoOperator

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The operator that defines how to search for people in the photos.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
var peopleInPhotoOperator: INConditionalOperator { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INConditionalOperator peopleInPhotoOperator;
```

*macOS*

```objc
@property (atomic, assign, readonly) INConditionalOperator peopleInPhotoOperator;
```

## Discussion

This property indicates whether the photo must contain all, some, or none of the people listed in the [`peopleInPhoto`](./peopleinphoto.md) property.

## See Also

### Getting the People in the Photos
- [var peopleInPhoto: [INPerson]?](./peopleinphoto.md)
  The people in the photos.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartphotoplaybackintent/peopleinphotooperator)*