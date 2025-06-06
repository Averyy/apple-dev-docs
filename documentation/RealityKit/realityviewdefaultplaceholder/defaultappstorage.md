# defaultAppStorage(_:)

**Framework**: RealityKit  
**Kind**: method

The default store used by `AppStorage` contained within the view.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewdefaultplaceholder/defaultappstorage(_:))*