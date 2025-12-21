# defaultAppStorage(_:)

**Framework**: SwiftUI  
**Kind**: method

The default store used by `AppStorage` contained within the view.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
nonisolated
func defaultAppStorage(_ store: UserDefaults) -> some View
```

#### Discussion

If unspecified, the default store for a view hierarchy is `UserDefaults.standard`, but can be set a to a custom one. For example, sharing defaults between an app and an extension can override the default store to one created with `UserDefaults.init(suiteName:_)`.

## Parameters

- `store`: The user defaults to use as the default   store for  .

## See Also

- [Restoring your app’s state with SwiftUI](restoring-your-app-s-state-with-swiftui.md)
  Provide app continuity for users by preserving their current activities.
- [struct AppStorage](appstorage.md)
  A property wrapper type that reflects a value from `UserDefaults` and invalidates a view on a change in value in that user default.
- [struct SceneStorage](scenestorage.md)
  A property wrapper type that reads and writes to persisted, per-scene storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/defaultappstorage(_:))*