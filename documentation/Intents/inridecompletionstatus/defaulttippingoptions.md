# defaultTippingOptions

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

An array of default tip amounts to display to the user.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var defaultTippingOptions: Set<INCurrencyAmount>? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, strong, readwrite, nullable) NSSet<INCurrencyAmount *> * defaultTippingOptions;
```

*macOS*

```objc
@property (atomic, strong, readwrite, nullable) NSSet<INCurrencyAmount *> * defaultTippingOptions;
```

#### Discussion

When requesting tip feedback, use this property to specify a set of default tip amounts. Specify up to three tip amounts. Siri or Maps display this information when gathering feedback from the user.

## See Also

### Requesting Feedback About the Ride
- [var feedbackType: INRideFeedbackTypeOptions](./feedbacktype.md)
  The type of feedback required for the ride before the user books a new ride can.
- [struct INRideFeedbackTypeOptions](../inridefeedbacktypeoptions.md)
  Constants indicating the type of feedback needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridecompletionstatus/defaulttippingoptions)*