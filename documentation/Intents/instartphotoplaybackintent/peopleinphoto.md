# peopleInPhoto

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The people in the photos.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
var peopleInPhoto: [INPerson]? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSArray<INPerson *> * peopleInPhoto;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSArray<INPerson *> * peopleInPhoto;
```

## Discussion

When this property contains one or more [`INPerson`](../inperson.md) objects, your search should return only photos that contain the specified people. Use the operator in the [`peopleInPhotoOperator`](./peopleinphotooperator.md) property to determine whether to search for photos containing all, some, or none of the specified people.

## See Also

### Getting the People in the Photos
- [var peopleInPhotoOperator: INConditionalOperator](./peopleinphotooperator.md)
  The operator that defines how to search for people in the photos.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartphotoplaybackintent/peopleinphoto)*