# navigationSubtitle(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Configures the view’s subtitle for purposes of navigation, using a localized string resource.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```swift
@export(implementation)
nonisolated func navigationSubtitle(_ subtitleKey: LocalizedStringResource) -> some View
```

**Other overloads**:

```swift
nonisolated
func navigationSubtitle(_ subtitle: Text) -> some View
```

```swift
nonisolated
func navigationSubtitle(_ subtitleKey: LocalizedStringKey) -> some View
```

```swift
nonisolated
func navigationSubtitle<S>(_ subtitle: S) -> some View where S : StringProtocol
```

## Discussion

A view’s navigation subtitle is used to provide additional contextual information alongside the navigation title. On macOS, the primary destination’s subtitle is displayed with the navigation title in the titlebar. On iOS and iPadOS, the subtitle is displayed with the navigation title in the navigation bar.

## Parameters

- `subtitleKey`: The key to a localized string to display.

## See Also

### Setting titles for navigation content
- [func navigationTitle(_:)](./navigationtitle%28_%29.md)
  Configures the view’s title for purposes of navigation, using a localized string resource.
- [func navigationDocument(_:)](./navigationdocument%28_%29.md)
  Configures the view’s document for purposes of navigation.
- [func navigationDocument(_:preview:)](./navigationdocument%28_,preview%29.md)
  Configures the view’s document for purposes of navigation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/navigationsubtitle(_:))*