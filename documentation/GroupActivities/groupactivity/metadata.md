# metadata

**Framework**: Group Activities  
**Kind**: property  
**Required**: Yes

A description of the activity, and optional image to display to the user.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var metadata: GroupActivityMetadata { get async }
```

#### Discussion

The system accesses this property when it’s ready to invite other participants to join the activity. Don’t access this property directly. Instead, implement it in your custom activity types and provide descriptive information about the current activity. For example, provide the title of the activity and an image that illustrates the activity.

## See Also

- [static var activityIdentifier: String](groupactivity/activityidentifier.md)
  An app-defined string that uniquely identifies the activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupactivity/metadata)*