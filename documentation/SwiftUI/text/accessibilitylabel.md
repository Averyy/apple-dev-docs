# accessibilityLabel(_:)

**Framework**: SwiftUI  
**Kind**: method

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
func accessibilityLabel(_ label: Text) -> Text
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

You can’t style the label that you add

## Parameters

- `label`: The text view to add the label to.

## See Also

- [func accessibilityHeading(AccessibilityHeadingLevel) -> Text](text/accessibilityheading(_:).md)
  Sets the accessibility level of this heading.
- [func accessibilityTextContentType(AccessibilityTextContentType) -> Text](text/accessibilitytextcontenttype(_:).md)
  Sets an accessibility text content type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/accessibilitylabel(_:))*