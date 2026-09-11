# init(typeIdentifier:value:)

**Framework**: App Intents Testing  
**Kind**: init

Creates an enumeration with a typed raw value.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
init(typeIdentifier: String, value: any LosslessStringConvertible)
```

## Parameters

- `typeIdentifier`: The enumeration type identifier.
- `value`: The raw, typed value that gets converted to a string representation.

## See Also

- [init(typeIdentifier: String, rawValue: String)](anyappenum/init(typeidentifier:rawvalue:).md)
  Creates a new instance with the specified enumeration identifier and raw value.
- [var typeIdentifier: String](anyappenum/typeidentifier.md)
  The enumeration’s type identifier.
- [var rawValue: String](anyappenum/rawvalue.md)
  The raw value of the selected enumeration option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/anyappenum/init(typeidentifier:value:))*