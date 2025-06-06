# toolbarRole(_:)

**Framework**: ManagedAppDistribution  
**Kind**: method

Configures the semantic role for the content populating the toolbar.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func toolbarRole(_ role: ToolbarRole) -> some View
```

#### Discussion

Use this modifier to configure the semantic role for content populating your app’s toolbar. SwiftUI uses this role when rendering the content of your app’s toolbar.

```None
ContentView()
    .navigationTitle("Browser")
    .toolbarRole(.browser)
    .toolbar {
        ToolbarItem(placement: .primaryAction) {
            AddButton()
        }
     }
```

## Parameters

- `role`: The role of the toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedappview/toolbarrole(_:))*