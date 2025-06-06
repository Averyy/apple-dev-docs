# uppercased()

**Framework**: Swift  
**Kind**: method

Returns an uppercase version of the string.

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
func uppercased() -> String
```

#### Return Value

An uppercase copy of the string.

#### Discussion

The following example transforms a string to uppercase letters:

```swift
let cafe = "Café 🍵"
print(cafe.uppercased())
// Prints "CAFÉ 🍵"
```

> **Note**: O()

## See Also

- [func lowercased() -> String](string/lowercased.md)
  Returns a lowercase version of the string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/uppercased())*