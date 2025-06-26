# location(category:)

**Framework**: RelevanceKit  
**Kind**: method

Tells the system a widget is relevant close to points of interest of a specific category.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
static func location(category: MKPointOfInterestCategory) -> RelevantContext?
```

#### Return Value

A contextual clue that the system uses to determine the relevance of a widget in the Smart Stack on Apple Watch.

#### Discussion

To indicate relevance at points of interest of a specific category, import [`MapKit`](https://developer.apple.com/documentation/MapKit) and request a person’s permission to access their location with the When in Use or Always access level. For more information on creating a widget that can access location information, refer to [`Accessing location information in widgets`](https://developer.apple.com/documentation/WidgetKit/Accessing-Location-Information-in-Widgets).

> **Note**: Smart Stacks are available in iOS, iPadOS, and watchOS. However, functionality provided by RelevanceKit API is only available in watchOS. Calling its API on other platforms doesn’t have any effect. For more information, refer to [`Increasing the visibility of widgets in Smart Stacks`](https://developer.apple.com/documentation/WidgetKit/Widget-Suggestions-In-Smart-Stacks).

## Parameters

- `category`: The points-of-interest category; for example, restaurants, parks, or stores.

## See Also

- [static func location(CLRegion) -> RelevantContext](relevantcontext/location(_:).md)
  Tells the system a widget is relevant at a specific location.
- [static func location(inferred: RelevantContext.InferredLocation) -> RelevantContext](relevantcontext/location(inferred:).md)
  Tells the system a widget is relevant at a person’s inferred location.
- [RelevantContext.InferredLocation](relevantcontext/inferredlocation.md)
  A structure with values for a person’s inferred home, work, school, and commute locations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/relevancekit/relevantcontext/location(category:))*