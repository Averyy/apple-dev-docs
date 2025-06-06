# DisclosureGroupStyleConfiguration

**Framework**: SwiftUI  
**Kind**: struct

The properties of a disclosure group instance.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
struct DisclosureGroupStyleConfiguration
```

## Topics

### Configuring the label
- [let label: DisclosureGroupStyleConfiguration.Label](disclosuregroupstyleconfiguration/label-swift.property.md)
  The label for the disclosure group.
- [DisclosureGroupStyleConfiguration.Label](disclosuregroupstyleconfiguration/label-swift.struct.md)
  A type-erased label of a disclosure group.
### Configuring the content
- [let content: DisclosureGroupStyleConfiguration.Content](disclosuregroupstyleconfiguration/content-swift.property.md)
  The content of the disclosure group.
- [DisclosureGroupStyleConfiguration.Content](disclosuregroupstyleconfiguration/content-swift.struct.md)
  A type-erased content of a disclosure group.
### Managing disclosure
- [var isExpanded: Bool](disclosuregroupstyleconfiguration/isexpanded.md)
  A binding to a Boolean that indicates whether the disclosure group is expanded.
- [var $isExpanded: Binding<Bool>](disclosuregroupstyleconfiguration/$isexpanded.md)

## See Also

- [func makeBody(configuration: Self.Configuration) -> Self.Body](disclosuregroupstyle/makebody(configuration:).md)
  Creates a view that represents the body of a disclosure group.
- [DisclosureGroupStyle.Configuration](disclosuregroupstyle/configuration.md)
  The properties of a disclosure group instance.
- [associatedtype Body : View](disclosuregroupstyle/body.md)
  A view that represents the body of a disclosure group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/disclosuregroupstyleconfiguration)*