# minSize(width:height:)

**Framework**: SwiftUI  
**Kind**: method

Sets the minimum size for the configuration.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func minSize(width: CGFloat? = nil, height: CGFloat? = nil) -> UIHostingConfiguration<Content, Background>
```

#### Discussion

Use this modifier to indicate that a configuration’s associated cell can be resized to a specific minimum. The following example allows the cell to be compressed to zero size:

```swift
UIHostingConfiguration {
    Text("My Contents")
}
.minSize(width: 0, height: 0)
```

## Parameters

- `width`: The value to use for the width dimension. A value of    indicates that the system default should be used.
- `height`: The value to use for the height dimension. A value   of   indicates that the system default should be used.

## See Also

- [func minSize() -> UIHostingConfiguration<Content, Background>](uihostingconfiguration/minsize.md)
  Sets the minimum size for the configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uihostingconfiguration/minsize(width:height:))*