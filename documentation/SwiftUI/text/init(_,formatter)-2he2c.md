# init(_:formatter:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a text view that displays the formatted representation of a reference-convertible value.

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
init<Subject>(_ subject: Subject, formatter: Formatter) where Subject : ReferenceConvertible
```

**Other overloads**:

```swift
init<Subject>(_ subject: Subject, formatter: Formatter) where Subject : NSObject
```

## Discussion

Use this initializer to create a text view that formats `subject` using `formatter`.

## Parameters

- `subject`: A [`ReferenceConvertible`](../../Foundation/referenceconvertible.md) instance compatible with `formatter`.
- `formatter`: A [`Formatter`](../../Foundation/formatter.md) capable of converting `subject` into a string representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/init(_:formatter:)-2he2c)*