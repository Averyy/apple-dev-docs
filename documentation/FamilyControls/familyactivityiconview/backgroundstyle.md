# backgroundStyle(_:)

**Framework**: FamilyControls  
**Kind**: method

Sets the specified style to render backgrounds within the view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func backgroundStyle<S>(_ style: S) -> some View where S : ShapeStyle
```

#### Discussion

The following example uses this modifier to set the `EnvironmentValues/backgroundStyle` environment value to a `ShapeStyle/blue` color that includes a subtle `Color/gradient`. SwiftUI fills the `Circle` shape that acts as a background element with this style:

```swift
Image(systemName: "swift")
    .padding()
    .background(in: Circle())
    .backgroundStyle(.blue.gradient)
```

To restore the default background style, set the `EnvironmentValues/backgroundStyle` environment value to `nil` using the `View/environment(_:_:)` modifer:

```swift
.environment(\.backgroundStyle, nil)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivityiconview/backgroundstyle(_:))*