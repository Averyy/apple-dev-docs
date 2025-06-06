# background(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the background contents for the hosting configuration’s enclosing cell.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func background<S>(_ style: S) -> UIHostingConfiguration<Content, _UIHostingConfigurationBackgroundView<S>> where S : ShapeStyle
```

#### Discussion

The following example sets a custom view to the background of the cell:

```swift
UIHostingConfiguration {
    Text("My Contents")
}
.background(Color.blue)
```

## Parameters

- `style`: The shape style to be used as the background of the   cell.

## See Also

- [func background<B>(content: () -> B) -> UIHostingConfiguration<Content, B>](uihostingconfiguration/background(content:).md)
  Sets the background contents for the hosting configuration’s enclosing cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uihostingconfiguration/background(_:))*