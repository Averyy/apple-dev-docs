# subscript(_:)

**Framework**: Swift  
**Kind**: subscript

Accesses the code unit at the given position.

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
subscript(idx: String.UTF16View.Index) -> UTF16.CodeUnit { get }
```

#### Overview

The following example uses the subscript to print the value of a string’s first UTF-16 code unit.

```swift
let greeting = "Hello, friend!"
let i = greeting.utf16.startIndex
print("First character's UTF-16 code unit: \(greeting.utf16[i])")
// Prints "First character's UTF-16 code unit: 72"
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/utf16view/subscript(_:)-5ta1h)*