# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a label representing the configuration of a style.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
nonisolated
init(_ configuration: LabelStyleConfiguration)
```

Available when `Title` is `LabelStyleConfiguration.Title` and `Icon` is `LabelStyleConfiguration.Icon`.

**Other overloads**:

```swift
nonisolated
init(_ applicationToken: ApplicationToken)
```

```swift
nonisolated
init(_ categoryToken: ActivityCategoryToken)
```

```swift
nonisolated
init(_ webDomainToken: WebDomainToken)
```

## Discussion

You can use this initializer within the [`makeBody(configuration:)`](../labelstyle/makebody%28configuration%29.md) method of a [`LabelStyle`](../labelstyle.md) instance to create an instance of the label that’s being styled. This is useful for custom label styles that only wish to modify the current style, as opposed to implementing a brand new style.

For example, the following style adds a red border around the label, but otherwise preserves the current style:

```swift
struct RedBorderedLabelStyle: LabelStyle {
    func makeBody(configuration: Configuration) -> some View {
        Label(configuration)
            .border(Color.red)
    }
}
```

## Parameters

- `configuration`: The label style to use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/label/init(_:)-2ue2r)*