# margins(_:_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the margins around the content of the configuration.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func margins(_ edges: Edge.Set = .all, _ insets: EdgeInsets) -> UIHostingConfiguration<Content, Background>
```

#### Discussion

Use this modifier to replace the default margins applied to the root of the configuration. The following example creates 10 points of space between the content and the background on the leading edge and 20 points of space on the trailing edge:

```swift
UIHostingConfiguration {
    Text("My Contents")
}
.margins(.horizontal, 20.0)
```

## Parameters

- `edges`: The edges to apply the insets. Any edges not specified will   use the system default values. The default value is   .
- `insets`: The insets to apply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uihostingconfiguration/margins(_:_:))*