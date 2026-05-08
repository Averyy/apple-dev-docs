# appTermination

**Framework**: SwiftUI  
**Kind**: property

Placement for commands that result in app termination.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static let appTermination: CommandGroupPlacement
```

#### Discussion

By default, this group includes the following command in macOS:

- Quit App

## See Also

- [static let appInfo: CommandGroupPlacement](commandgroupplacement/appinfo.md)
  Placement for commands that provide information about the app, the terms of the user’s license agreement, and so on.
- [static let appSettings: CommandGroupPlacement](commandgroupplacement/appsettings.md)
  Placement for commands that expose app settings and preferences.
- [static let appVisibility: CommandGroupPlacement](commandgroupplacement/appvisibility.md)
  Placement for commands that control the visibility of running apps.
- [static let systemServices: CommandGroupPlacement](commandgroupplacement/systemservices.md)
  Placement for commands that expose services other apps provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/commandgroupplacement/apptermination)*