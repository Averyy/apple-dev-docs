# background(content:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the background contents for the hosting configuration’s enclosing cell.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func background<B>(@ContentBuilder content: () -> B) -> UIHostingConfiguration<Content, B> where B : View
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

## Parameters

- `content`: The contents of the SwiftUI hierarchy to be shown inside the background of the cell.

## See Also

### Setting the background
- [func background<S>(S) -> UIHostingConfiguration<Content, _UIHostingConfigurationBackgroundView<S>>](./background%28_%29.md)
  Sets the background contents for the hosting configuration’s enclosing cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uihostingconfiguration/background(content:))*