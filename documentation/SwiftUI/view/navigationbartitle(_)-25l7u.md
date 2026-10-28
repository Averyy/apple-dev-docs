# navigationBarTitle(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the title of this view’s navigation bar with a string.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2 (renamed: navigationTitle(_:))
- iPadOS 13.0+ - Deprecated in 27.2 (renamed: navigationTitle(_:))
- Mac Catalyst 13.0+ - Deprecated in 27.2 (renamed: navigationTitle(_:))
- tvOS 13.0+ - Deprecated in 27.2 (renamed: navigationTitle(_:))
- visionOS 1.0+ - Deprecated in 27.2 (renamed: navigationTitle(_:))
- watchOS 6.0+ - Deprecated in 27.2 (renamed: navigationTitle(_:))

> **Deprecated**: Use [`navigationTitle(_:)`](./navigationtitle%28_%29-avgj.md) instead.

## Declaration

```swift
nonisolated
func navigationBarTitle<S>(_ title: S) -> some View where S : StringProtocol
```

**Other overloads**:

```swift
nonisolated
func navigationBarTitle(_ title: Text) -> some View
```

```swift
nonisolated
func navigationBarTitle(_ titleKey: LocalizedStringKey) -> some View
```

## Discussion

Use `navigationBarTitle(_:)` to set the title of the navigation bar using a `String`. This modifier only takes effect when this view is inside of and visible within a [`NavigationView`](../navigationview.md).

In the example below, text for the navigation bar title is provided using a string:

```swift
struct FlavorView: View {
    let items = ["Chocolate", "Vanilla", "Strawberry", "Mint Chip",
                 "Pistachio"]
    let text = "Today's Flavors"
    var body: some View {
        NavigationView {
            List(items, id: \.self) {
                Text($0)
            }
            .navigationBarTitle(text)
        }
    }
}
```

## Parameters

- `title`: A title for this view to display in the navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/navigationbartitle(_:)-25l7u)*