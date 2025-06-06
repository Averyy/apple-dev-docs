# init(style:locale:)

**Framework**: Foundation  
**Kind**: init

Creates an instance using the provided format style and locale.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
init(style: PersonNameComponents.FormatStyle.Style = .medium, locale: Locale = .autoupdatingCurrent)
```

#### Discussion

Customize the person name components format style by providing a style and a locale.

The formatted style can be long, medium, short, or abbreviated. The default value is [`PersonNameComponents.FormatStyle.Style.medium`](personnamecomponents/formatstyle/style-swift.enum/medium.md).

The locale provides linguistic and cultural context to the formatted name. The default value is [`autoupdatingCurrent`](locale/autoupdatingcurrent.md).

## Parameters

- `style`: The   used to format the name.
- `locale`: The   used to create the string representation of the name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/personnamecomponents/formatstyle/init(style:locale:))*