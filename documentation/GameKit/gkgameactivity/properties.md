# properties

**Framework**: GameKit  
**Kind**: property

Properties that contain additional information about the activity.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var properties: [String : String] { get set }
```

#### Discussion

This takes precedence over the `defaultProperties` on the `activityDefinition`.

1. This dictionary is initialized with the default properties from the activity definition and deep linked properties if any.
2. If deep linking contains the same key as the default properties, the deep linked value will override the default value.
3. The properties can be updated at runtime.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgameactivity/properties)*