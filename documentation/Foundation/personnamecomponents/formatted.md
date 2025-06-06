# formatted(_:)

**Framework**: Foundation  
**Kind**: method

Generates a locale-aware string representation of an instance of person name components using the provided format style.

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
func formatted<S>(_ style: S) -> S.FormatOutput where S : FormatStyle, S.FormatInput == PersonNameComponents
```

#### Return Value

A string, formatted according to the provided style.

#### Discussion

Use the [`formatted(_:)`](personnamecomponents/formatted(_:).md) method to create a string representation of a person’s name with a customized length for specific uses. You can use the [`PersonNameComponents.FormatStyle`](personnamecomponents/formatstyle.md) static factory method [`name(style:)`](formatstyle/name(style:).md) to create a custom format style as a parameter to the method.

For example:

```swift
var tlc = PersonNameComponents()
tlc.familyName = "Clark"
tlc.givenName = "Thomas"
tlc.middleName = "Louis"
tlc.namePrefix = "Dr."
tlc.nickname = "Tom"
tlc.nameSuffix = "Esq."

tlc.formatted(.name(style: .long))
// Dr. Thomas Louis Clark Esq.

tlc.formatted(.name(style: .medium))
// Thomas Clark

tlc.formatted(.name(style: .short))
// Tom

tlc.formatted(.name(style: .abbreviated))
// TC
```

## Parameters

- `style`: Specifies the   applied to the person name components.

## See Also

- [func formatted() -> String](personnamecomponents/formatted.md)
  Generates a locale-aware string representation of an instance of person name components using the default format style.
- [PersonNameComponents.FormatStyle](personnamecomponents/formatstyle.md)
  A type used to format a person’s name with a style appropriate for the given locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/personnamecomponents/formatted(_:))*