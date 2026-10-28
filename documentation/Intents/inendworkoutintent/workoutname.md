# workoutName

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The name of the workout.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
@NSCopying
var workoutName: INSpeakableString? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INSpeakableString * workoutName;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INSpeakableString * workoutName;
```

## Discussion

If the user ended a specific workout, this property contains the name of that workout. The workout name can be user-specified, a workout name defined in your app’s global vocabulary file, or a custom user-spoken workout name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inendworkoutintent/workoutname)*