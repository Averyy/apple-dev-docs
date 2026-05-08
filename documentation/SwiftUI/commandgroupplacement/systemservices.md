# systemServices

**Framework**: SwiftUI  
**Kind**: property

Placement for commands that expose services other apps provide.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static let systemServices: CommandGroupPlacement
```

#### Discussion

By default, this group includes the following command in macOS:

- Services submenu (managed automatically)

## See Also

- [static let appInfo: CommandGroupPlacement](commandgroupplacement/appinfo.md)
  Placement for commands that provide information about the app, the terms of the user’s license agreement, and so on.
- [static let appSettings: CommandGroupPlacement](commandgroupplacement/appsettings.md)
  Placement for commands that expose app settings and preferences.
- [static let appTermination: CommandGroupPlacement](commandgroupplacement/apptermination.md)
  Placement for commands that result in app termination.
- [static let appVisibility: CommandGroupPlacement](commandgroupplacement/appvisibility.md)
  Placement for commands that control the visibility of running apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/commandgroupplacement/systemservices)*