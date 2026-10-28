# navigationTitle(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Configures the view’s title for purposes of navigation, using a string binding.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func navigationTitle(_ title: Binding<String>) -> some View
```

**Other overloads**:

```swift
@export(implementation)
nonisolated func navigationTitle(_ titleResource: LocalizedStringResource) -> some View
```

```swift
nonisolated
func navigationTitle(_ title: Text) -> some View
```

```swift
nonisolated
func navigationTitle(_ titleKey: LocalizedStringKey) -> some View
```

```swift
nonisolated
func navigationTitle<S>(_ title: S) -> some View where S : StringProtocol
```

```swift
nonisolated
func navigationTitle<V>(@ContentBuilder _ title: () -> V) -> some View where V : View
```

## Discussion

In iOS, iPadOS, and macOS, this allows editing the navigation title when the title is displayed in the toolbar.

Refer to the [Configure your apps navigation titles](../configure-your-apps-navigation-titles.md) article for more information on navigation title modifiers.

## Parameters

- `title`: The text of the title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/navigationtitle(_:)-7onr8)*