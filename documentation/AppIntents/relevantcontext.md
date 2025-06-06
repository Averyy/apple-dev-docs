# RelevantContext

**Framework**: App Intents  
**Kind**: struct

A type that specifies conditions for relevance.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
struct RelevantContext
```

## Topics

### Structures
- [RelevantContext.FitnessCondition](relevantcontext/fitnesscondition.md)
- [RelevantContext.HeadphonesCondition](relevantcontext/headphonescondition.md)
- [RelevantContext.InferredLocation](relevantcontext/inferredlocation.md)
- [RelevantContext.SleepCondition](relevantcontext/sleepcondition.md)
### Type Methods
- [static func date(Date) -> RelevantContext](relevantcontext/date(_:).md)
  An exact point in time, such as the start of a sporting event or a live broadcast.
- [static func date(from: Date, to: Date) -> RelevantContext](relevantcontext/date(from:to:).md)
  An exact range in time: similar uses as `date()`, but with a known endpoint.
- [static func fitness(RelevantContext.FitnessCondition) -> RelevantContext](relevantcontext/fitness(_:).md)
  Fitness.
- [static func hardware(headphones: RelevantContext.HeadphonesCondition) -> RelevantContext](relevantcontext/hardware(headphones:).md)
  Hardware
- [static func location(CLRegion) -> RelevantContext](relevantcontext/location(_:).md)
  An exact region.  To create a region based on a point location or an address, see CoreLocation.
- [static func location(inferred: RelevantContext.InferredLocation) -> RelevantContext](relevantcontext/location(inferred:).md)
  An abstract location, inferred from user behavior.
- [static func sleep(RelevantContext.SleepCondition) -> RelevantContext](relevantcontext/sleep(_:).md)
  Sleep

## See Also

- [struct RelevantIntent](relevantintent.md)
  A type that specifies an intent and its relevance to the user.
- [class RelevantIntentManager](relevantintentmanager.md)
  A type that saves relevant intents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/relevantcontext)*