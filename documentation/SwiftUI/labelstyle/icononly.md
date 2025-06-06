# iconOnly

**Framework**: SwiftUI  
**Kind**: property

A label style that only displays the icon of the label.

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
@MainActor
@preconcurrency static var iconOnly: IconOnlyLabelStyle { get }
```

#### Discussion

The title of the label is still used for non-visual descriptions, such as VoiceOver.

## See Also

- [static var automatic: DefaultLabelStyle](labelstyle/automatic.md)
  A label style that resolves its appearance automatically based on the current context.
- [static var titleAndIcon: TitleAndIconLabelStyle](labelstyle/titleandicon.md)
  A label style that shows both the title and icon of the label using a system-standard layout.
- [static var titleOnly: TitleOnlyLabelStyle](labelstyle/titleonly.md)
  A label style that only displays the title of the label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/labelstyle/icononly)*