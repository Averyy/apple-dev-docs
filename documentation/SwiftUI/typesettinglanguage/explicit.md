# explicit(_:)

**Framework**: SwiftUI  
**Kind**: method

Use explicit language.

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
static func explicit(_ language: Locale.Language) -> TypesettingLanguage
```

#### Return Value

A `TypesettingLanguage`.

#### Discussion

An explicit language will be used for typesetting. For example, if used with Thai language the line heights will be as tall as needed to accommodate Thai.

## Parameters

- `language`: The language to use for typesetting.

## See Also

- [static let automatic: TypesettingLanguage](typesettinglanguage/automatic.md)
  Automatic language behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/typesettinglanguage/explicit(_:))*