# automatic

**Framework**: SwiftUI  
**Kind**: property

Automatic language behavior.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
static let automatic: TypesettingLanguage
```

#### Discussion

When determining the language to use for typesetting the current UI language and preferred languages will be considered. For example, if the current UI locale is for English and Thai is included in the preferred languages then line heights will be taller to accommodate the taller glyphs used by Thai.

## See Also

- [static func explicit(Locale.Language) -> TypesettingLanguage](typesettinglanguage/explicit(_:).md)
  Use explicit language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/typesettinglanguage/automatic)*