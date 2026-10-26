# feedbackType

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The type of feedback required for the ride before the user books a new ride can.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var feedbackType: INRideFeedbackTypeOptions { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INRideFeedbackTypeOptions feedbackType;
```

*macOS*

```objc
@property (atomic, assign, readonly) INRideFeedbackTypeOptions feedbackType;
```

## See Also

### Requesting Feedback About the Ride
- [struct INRideFeedbackTypeOptions](../inridefeedbacktypeoptions.md)
  Constants indicating the type of feedback needed.
- [var defaultTippingOptions: Set<INCurrencyAmount>?](./defaulttippingoptions.md)
  An array of default tip amounts to display to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridecompletionstatus/feedbacktype)*