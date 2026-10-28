# appendInterpolation(_:formatter:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Appends an optionally-formatted instance of a Foundation type to a string interpolation.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
mutating func appendInterpolation<Subject>(_ subject: Subject, formatter: Formatter? = nil) where Subject : ReferenceConvertible
```

**Other overloads**:

```swift
mutating func appendInterpolation<Subject>(_ subject: Subject, formatter: Formatter? = nil) where Subject : NSObject
```

## Discussion

Don’t call this method directly; it’s used by the compiler when interpreting string interpolations.

## Parameters

- `subject`: The Foundation object to append.
- `formatter`: A formatter to convert `subject` to a string representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/localizedstringkey/stringinterpolation/appendinterpolation(_:formatter:)-9vdw4)*