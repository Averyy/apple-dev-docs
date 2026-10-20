# location(category:)

**Framework**: RelevanceKit  
**Kind**: method  
**Role**: Type Method

Tells the system a widget is relevant close to points of interest of a specific category.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
static func location(category: MKPointOfInterestCategory) -> RelevantContext?
```

#### Return Value

A contextual clue that the system uses to determine the relevance of a widget in the Smart Stack on Apple Watch, or `nil` if the category is not supported.

#### Discussion

To indicate relevance at points of interest of a specific category, import [MapKit](../../MapKit/MapKit.md) and request a person’s permission to access their location with the When in Use or Always access level. For more information on creating a widget that can access location information, refer to [Accessing location information in widgets](../../WidgetKit/accessing-location-information-in-widgets.md).

> **Note**: Smart Stacks are available in iOS, iPadOS, and watchOS. However, functionality provided by RelevanceKit API is only available in watchOS. Calling its API on other platforms doesn’t have any effect. For more information, refer to [Increasing the visibility of widgets in Smart Stacks](../../WidgetKit/widget-suggestions-in-smart-stacks.md).

## Parameters

- `category`: The points-of-interest category; for example, restaurants, parks, or stores.

## See Also

### Location clues
- [static func location(CLRegion) -> RelevantContext](./location%28_%29.md)
  Tells the system a widget is relevant at a specific location.
- [static func location(inferred: RelevantContext.InferredLocation) -> RelevantContext](./location%28inferred%29.md)
  Tells the system a widget is relevant at a person’s inferred location.
- [RelevantContext.InferredLocation](./inferredlocation.md)
  A structure with values for a person’s inferred home, work, school, and commute locations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/relevancekit/relevantcontext/location(category:))*