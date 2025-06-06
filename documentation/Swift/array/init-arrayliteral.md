# init(arrayLiteral:)

**Framework**: Swift  
**Kind**: init

Creates an array from the given array literal.

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
init(arrayLiteral elements: Element...)
```

#### Discussion

Do not call this initializer directly. It is used by the compiler when you use an array literal. Instead, create a new array by using an array literal as its value. To do this, enclose a comma-separated list of values in square brackets.

Here, an array of strings is created from an array literal holding only strings.

```swift
let ingredients = ["cocoa beans", "sugar", "cocoa butter", "salt"]
```

## Parameters

- `elements`: A variadic list of elements of the new array.

## See Also

- [var hashValue: Int](array/hashvalue.md)
  The hash value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/init(arrayliteral:))*