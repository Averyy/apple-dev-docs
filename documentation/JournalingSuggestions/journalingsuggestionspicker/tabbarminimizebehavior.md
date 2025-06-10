# tabBarMinimizeBehavior(_:)

**Framework**: Journaling Suggestions  
**Kind**: method

Sets the behavior for tab bar minimization.

**Availability**:
- iOS 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func tabBarMinimizeBehavior(_ behavior: TabBarMinimizeBehavior) -> some View
```

#### Discussion

The following TabView minimizes its tab bar when scrolling in the ‘Numbers’ or ‘Alerts’ tabs on iPhone.

```None
struct ContentView: View {
    var body: some View {
         TabView {
             Tab("Numbers", systemImage: "number") {
                 ScrollView {
                    ForEach(0 ..< 50) { index in
                        Text("\(index)")
                            .padding()
                    }
                 }
             }
             Tab("Alerts", systemImage: "bell") {
                 AlertsView()
             }
         }
         .tabBarMinimizeBehavior(.onScrollDown)
    }
}
```

## Parameters

- `behavior`: The minimize behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionspicker/tabbarminimizebehavior(_:))*