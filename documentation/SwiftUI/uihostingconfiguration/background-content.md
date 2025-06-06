# background(content:)

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
func background<B>(@ViewBuilder content: () -> B) -> UIHostingConfiguration<Content, B> where B : View
```

#### Discussion

The following example sets a custom view to the background of the cell:

```swift
UIHostingConfiguration {
    Text("My Contents")
}
.background {
    MyBackgroundView()
}
```

## See Also

- [func background<S>(S) -> UIHostingConfiguration<Content, _UIHostingConfigurationBackgroundView<S>>](uihostingconfiguration/background(_:).md)
  Sets the background contents for the hosting configuration’s enclosing cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uihostingconfiguration/background(content:))*