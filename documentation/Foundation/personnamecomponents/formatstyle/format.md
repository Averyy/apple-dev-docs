# format(_:)

**Framework**: Foundation  
**Kind**: method

Creates a string representation from a person name components value.

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
func format(_ value: PersonNameComponents) -> String
```

#### Return Value

A string representation of the person name components.

#### Discussion

The [`format(_:)`](personnamecomponents/formatstyle/format(_:).md) instance method applies the style to an instance of `PersonNameComponent`. After creating a style, you can use it to format multiple instances of person name components. For example:

```swift
let customPersonFormatStyle = PersonNameComponents.FormatStyle(style: .medium, locale: Locale(identifier: "us_EN"))

var person1 = PersonNameComponents()
person1.familyName = "Clark"
person1.givenName = "Thomas"
person1.middleName = "Louis"
person1.namePrefix = "Dr."
person1.nickname = "Tom"
person1.nameSuffix = "Esq."

let customPersonString1 = 
customPersonFormatStyle.format(person1)
// Thomas Clark

let customPersonString2 = 
customPersonFormatStyle.format(person2)
// Maria Ruiz
```

## Parameters

- `value`: The person name components object to format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/personnamecomponents/formatstyle/format(_:))*