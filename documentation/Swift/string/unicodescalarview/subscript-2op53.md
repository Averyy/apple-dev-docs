# subscript(_:)

**Framework**: Swift  
**Kind**: subscript

Accesses the Unicode scalar value at the given position.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
subscript(position: String.UnicodeScalarView.Index) -> Unicode.Scalar { get }
```

#### Overview

The following example searches a string’s Unicode scalars view for a capital letter and then prints the character and Unicode scalar value at the found index:

```swift
let greeting = "Hello, friend!"
if let i = greeting.unicodeScalars.firstIndex(where: { "A"..."Z" ~= $0 }) {
    print("First capital letter: \(greeting.unicodeScalars[i])")
    print("Unicode scalar value: \(greeting.unicodeScalars[i].value)")
}
// Prints "First capital letter: H"
// Prints "Unicode scalar value: 72"
```

## Parameters

- `position`: A valid index of the character view.    must be less than the view’s end index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/unicodescalarview/subscript(_:)-2op53)*