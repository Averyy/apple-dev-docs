# buildIf(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

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
static func buildIf<Content>(_ content: Content?) -> Content? where Content : CustomizableToolbarContent
```

**Other overloads**:

```swift
static func buildIf<Content>(_ content: Content?) -> Content? where Content : ToolbarContent
```

## See Also

### Building conditional toolbar content
- [static buildEither(first:)](./buildeither%28first%29.md)
- [static buildEither(second:)](./buildeither%28second%29.md)
- [static buildExpression(_:)](./buildexpression%28_%29.md)
  Builds an expression within the builder.
- [static buildLimitedAvailability(_:)](./buildlimitedavailability%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbarcontentbuilder/buildif(_:))*