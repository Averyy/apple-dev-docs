# location(inferred:)

**Framework**: RelevanceKit  
**Kind**: method

Tells the system a widget is relevant at a person’s inferred location.

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
static func location(inferred: RelevantContext.InferredLocation) -> RelevantContext
```

#### Return Value

A contextual clue that the system uses to determine the relevance of a widget in the Smart Stack on Apple Watch.

#### Discussion

To indicate relevance at an inferred location, request a person’s permission to access their location with the When in Use or Always access level. For more information on creating a widget that can access location information, refer to [`Accessing location information in widgets`](https://developer.apple.com/documentation/WidgetKit/Accessing-Location-Information-in-Widgets).

> **Note**: Smart Stacks are available in iOS, iPadOS, and watchOS. However, functionality provided by RelevanceKit API is only available in watchOS. Calling its API on other platforms doesn’t have any effect. For more information, refer to [`Increasing the visibility of widgets in Smart Stacks`](https://developer.apple.com/documentation/WidgetKit/Widget-Suggestions-In-Smart-Stacks).

## Parameters

- `inferred`: Location information that the system infers from a person’s behavior. For example, the system could infer   that a person is at work or at school.

## See Also

- [static func location(CLRegion) -> RelevantContext](relevantcontext/location(_:).md)
  Tells the system a widget is relevant at a specific location.
- [RelevantContext.InferredLocation](relevantcontext/inferredlocation.md)
  A structure with values for a person’s inferred home, work, school, and commute locations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/relevancekit/relevantcontext/location(inferred:))*