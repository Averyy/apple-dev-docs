# navigationBarTitle(_:)

**Framework**: ManagedAppDistribution  
**Kind**: method

Sets the title in the navigation bar for this view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func navigationBarTitle(_ title: Text) -> some View
```

#### Discussion

Use `navigationBarTitle(_:)` to set the title of the navigation bar. This modifier only takes effect when this view is inside of and visible within a `NavigationView`.

The example below shows setting the title of the navigation bar using a `Text` view:

```None
struct FlavorView: View {
    let items = ["Chocolate", "Vanilla", "Strawberry", "Mint Chip",
                 "Pistachio"]
    var body: some View {
        NavigationView {
            List(items, id: \.self) {
                Text($0)
            }
            .navigationBarTitle(Text("Today's Flavors"))
        }
    }
}
```

## Parameters

- `title`: A description of this view to display in the   navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedcontentview/navigationbartitle(_:)-9akdh)*