# glassEffectTransition(_:isEnabled:)

**Framework**: Assignables  
**Kind**: method

Associates a glass effect transition with any glass effects defined within this view.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency func glassEffectTransition(_ transition: GlassEffectTransition, isEnabled: Bool = true) -> some View
```

#### Discussion

You use this modifier with the `View/glassEffect(_:in:isEnabled:)` view modifier and `GlassEffectContainer` view. When used together, SwiftUI will use the provided transition to apply changes to the glass effect when you add or remove views with these effects from the view hierarchy.

In the example below, the notepad image will transition into and out of the pencil image when the isExpanded variable changes.

```None
var isExpanded: Bool
@Namespace private var namespace

var body: some View {
    GlassEffectContainer(spacing: 10.0) {
        HStack(spacing: 10.0) {
            Image(systemName: "pencil")
                .frame(width: 20.0, height: 20.0)
                .glassEffect()
                .glassEffectID("pencil", in: namespace)

                if isExpanded {
                    Image(systemName: "note")
                        .frame(width: 20.0, height: 20.0)
                        .glassEffect()
                        .glassEffectID("note", in: namespace)
                        .glassEffectTransition(.matchedGeometry)
                }
            }
        }
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocumentview/glasseffecttransition(_:isenabled:))*