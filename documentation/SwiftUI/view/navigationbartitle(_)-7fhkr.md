# navigationBarTitle(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the title of this view’s navigation bar with a localized string.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2 (renamed: navigationTitle(_:))
- iPadOS 13.0+ - Deprecated in 27.2 (renamed: navigationTitle(_:))
- Mac Catalyst 13.0+ - Deprecated in 27.2 (renamed: navigationTitle(_:))
- tvOS 13.0+ - Deprecated in 27.2 (renamed: navigationTitle(_:))
- visionOS 1.0+ - Deprecated in 27.2 (renamed: navigationTitle(_:))
- watchOS 6.0+ - Deprecated in 27.2 (renamed: navigationTitle(_:))

> **Deprecated**: Use [`navigationTitle(_:)`](./navigationtitle%28_%29-43srq.md) instead.

## Declaration

```swift
nonisolated
func navigationBarTitle(_ titleKey: LocalizedStringKey) -> some View
```

**Other overloads**:

```swift
nonisolated
func navigationBarTitle(_ title: Text) -> some View
```

```swift
nonisolated
func navigationBarTitle<S>(_ title: S) -> some View where S : StringProtocol
```

## Discussion

Use `navigationBarTitle(_:)` to set the title of the navigation bar using a [`LocalizedStringKey`](../localizedstringkey.md) that will be used to search for a matching localized string in the application’s localizable strings assets.

This modifier only takes effect when this view is inside of and visible within a [`NavigationView`](../navigationview.md).

In the example below, a string constant is used to access a [`LocalizedStringKey`](../localizedstringkey.md) that will be resolved at run time to provide a title for the navigation bar. If the localization key cannot be resolved, the text of the key name will be used as the title text.

```swift
struct FlavorView: View {
    let items = ["Chocolate", "Vanilla", "Strawberry", "Mint Chip",
                 "Pistachio"]
    var body: some View {
        NavigationView {
            List(items, id: \.self) {
                Text($0)
            }
            .navigationBarTitle("Today's Flavors")
        }
    }
}
```

## Parameters

- `titleKey`: A key to a localized description of this view to display in the navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/navigationbartitle(_:)-7fhkr)*