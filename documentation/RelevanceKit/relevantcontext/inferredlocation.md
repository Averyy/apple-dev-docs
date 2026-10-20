# RelevantContext.InferredLocation

**Framework**: RelevanceKit  
**Kind**: struct  
**Role**: Structure

A structure with values for a person’s inferred home, work, school, and commute locations.

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
struct InferredLocation
```

## Topics

### Conditions
- [static var commute: RelevantContext.InferredLocation](./inferredlocation/commute.md)
  A person’s commute between two inferred locations.
- [static var home: RelevantContext.InferredLocation](./inferredlocation/home.md)
  A person’s inferred home location.
- [static var school: RelevantContext.InferredLocation](./inferredlocation/school.md)
  A person’s inferred school location.
- [static var work: RelevantContext.InferredLocation](./inferredlocation/work.md)
  A person’s inferred work location.

## See Also

### Location clues
- [static func location(CLRegion) -> RelevantContext](./location%28_%29.md)
  Tells the system a widget is relevant at a specific location.
- [static func location(inferred: RelevantContext.InferredLocation) -> RelevantContext](./location%28inferred%29.md)
  Tells the system a widget is relevant at a person’s inferred location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/relevancekit/relevantcontext/inferredlocation)*