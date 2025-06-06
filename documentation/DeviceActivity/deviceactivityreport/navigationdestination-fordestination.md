# navigationDestination(for:destination:)

**Framework**: DeviceActivity  
**Kind**: method

Associates a destination view with a presented data type for use within a navigation stack.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func navigationDestination<D, C>(for data: D.Type, @ViewBuilder destination: @escaping (D) -> C) -> some View where D : Hashable, C : View
```

#### Discussion

Add this view modifier to a view inside a `NavigationStack` to describe the view that the stack displays when presenting a particular kind of data. Use a `NavigationLink` to present the data. For example, you can present a `ColorDetail` view for each presentation of a `Color` instance:

```swift
NavigationStack {
    List {
        NavigationLink("Mint", value: Color.mint)
        NavigationLink("Pink", value: Color.pink)
        NavigationLink("Teal", value: Color.teal)
    }
    .navigationDestination(for: Color.self) { color in
        ColorDetail(color: color)
    }
    .navigationTitle("Colors")
}
```

You can add more than one navigation destination modifier to the stack if it needs to present more than one kind of data.

Do not put a navigation destination modifier inside a “lazy” container, like `List` or `LazyVStack`. These containers create child views only when needed to render on screen. Add the navigation destination modifier outside these containers so that the navigation stack can always see the destination.

## Parameters

- `data`: The type of data that this destination matches.
- `destination`: A view builder that defines a view to display   when the stack’s navigation state contains a value of   type  . The closure takes one argument, which is the value   of the data to present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityreport/navigationdestination(for:destination:))*