# labelStyle(_:)

**Framework**: App Intents  
**Kind**: method

Sets the style for labels within this view.

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
func labelStyle<S>(_ style: S) -> some View where S : LabelStyle
```

#### Discussion

Use this modifier to set a specific style for all labels within a view:

```swift
VStack {
    Label("Fire", systemImage: "flame.fill")
    Label("Lightning", systemImage: "bolt.fill")
}
.labelStyle(MyCustomLabelStyle())
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/shortcutslink/labelstyle(_:))*