# accessibilityLabel(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Adds a label to the view that describes its contents.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func accessibilityLabel<S>(_ label: S) -> Text where S : StringProtocol
```

**Other overloads**:

```swift
@export(implementation)
nonisolated func accessibilityLabel(_ label: LocalizedStringResource) -> Text
```

```swift
nonisolated
func accessibilityLabel(_ label: Text) -> Text
```

```swift
nonisolated
func accessibilityLabel(_ labelKey: LocalizedStringKey) -> Text
```

## Discussion

Use this method to provide an alternative accessibility label to the text that is displayed. For example, you can give an alternate label to a navigation title:

```swift
var body: some View {
    NavigationView {
        ContentView()
            .navigationTitle(Text("􀈤").accessibilityLabel("Inbox"))
    }
}
```

## Parameters

- `label`: The string for the alternative accessibility label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/accessibilitylabel(_:)-6l0ln)*