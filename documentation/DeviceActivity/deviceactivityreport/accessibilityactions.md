# accessibilityActions(_:)

**Framework**: DeviceActivity  
**Kind**: method

Adds multiple accessibility actions to the view.

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
func accessibilityActions<Content>(@ViewBuilder _ content: () -> Content) -> some View where Content : View
```

#### Discussion

Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. For example, this is how a dynamic number of custom action could be added to a view.

```swift
var isDraft: Bool

var body: some View {
    ContentView()
        .accessibilityActions {
            ForEach(actions) { action in
                Button {
                    action()
                } label: {
                    Text(action.title)
                }
            }

            if isDraft {
                Button {
                    // Handle Delete
                } label: {
                    Text("Delete")
                }
            }
        }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityreport/accessibilityactions(_:))*