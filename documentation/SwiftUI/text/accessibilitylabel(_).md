# accessibilityLabel(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Adds a label to the view that describes its contents.

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
@export(implementation)
nonisolated func accessibilityLabel(_ label: LocalizedStringResource) -> Text
```

**Other overloads**:

```swift
nonisolated
func accessibilityLabel(_ label: Text) -> Text
```

```swift
nonisolated
func accessibilityLabel(_ labelKey: LocalizedStringKey) -> Text
```

```swift
nonisolated
func accessibilityLabel<S>(_ label: S) -> Text where S : StringProtocol
```

#### Discussion

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

- `label`: The string resource for the alternative accessibility label.

## See Also

### Providing accessibility information
- [func accessibilityHeading(AccessibilityHeadingLevel) -> Text](./accessibilityheading%28_%29.md)
  Sets the accessibility level of this heading.
- [func accessibilityTextContentType(AccessibilityTextContentType) -> Text](./accessibilitytextcontenttype%28_%29.md)
  Sets an accessibility text content type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/accessibilitylabel(_:))*