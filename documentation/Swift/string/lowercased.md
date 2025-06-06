# lowercased()

**Framework**: Swift  
**Kind**: method

Returns a lowercase version of the string.

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
func lowercased() -> String
```

#### Return Value

A lowercase copy of the string.

#### Discussion

Here’s an example of transforming a string to all lowercase letters.

```swift
let cafe = "BBQ Café 🍵"
print(cafe.lowercased())
// Prints "bbq café 🍵"
```

> **Note**: O()

## See Also

- [func uppercased() -> String](string/uppercased.md)
  Returns an uppercase version of the string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/lowercased())*