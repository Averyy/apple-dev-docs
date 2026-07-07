# supportedActivityFamilies

**Framework**: SwiftUI  
**Kind**: property

An environment value that that indicates potential rendered family for a Live Activity.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
var supportedActivityFamilies: Set<ActivityFamily> { get set }
```

#### Discussion

To detect the currently rendered activity family size, use the [`activityFamily`](EnvironmentValues/activityFamily.md) environment variable. The `supportedActivityFamilies` environment value might only be useful if your make you make your Live Activity views available in a Swift package.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/supportedactivityfamilies)*