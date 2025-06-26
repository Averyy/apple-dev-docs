# RelevantContext.InferredLocation

**Framework**: RelevanceKit  
**Kind**: struct

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
- [static var commute: RelevantContext.InferredLocation](relevantcontext/inferredlocation/commute.md)
  A person’s commute between two inferred locations.
- [static var home: RelevantContext.InferredLocation](relevantcontext/inferredlocation/home.md)
  A person’s inferred home location.
- [static var school: RelevantContext.InferredLocation](relevantcontext/inferredlocation/school.md)
  A person’s inferred school location.
- [static var work: RelevantContext.InferredLocation](relevantcontext/inferredlocation/work.md)
  A person’s inferred work location.

## See Also

- [static func location(CLRegion) -> RelevantContext](relevantcontext/location(_:).md)
  Tells the system a widget is relevant at a specific location.
- [static func location(inferred: RelevantContext.InferredLocation) -> RelevantContext](relevantcontext/location(inferred:).md)
  Tells the system a widget is relevant at a person’s inferred location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/relevancekit/relevantcontext/inferredlocation)*