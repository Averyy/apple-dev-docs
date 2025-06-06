# init(dictionaryLiteral:)

**Framework**: Swift  
**Kind**: init

Creates a dictionary initialized with a dictionary literal.

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
init(dictionaryLiteral elements: (Key, Value)...)
```

#### Discussion

Do not call this initializer directly. It is called by the compiler to handle dictionary literals. To use a dictionary literal as the initial value of a dictionary, enclose a comma-separated list of key-value pairs in square brackets.

For example, the code sample below creates a dictionary with string keys and values.

```swift
let countryCodes = ["BR": "Brazil", "GH": "Ghana", "JP": "Japan"]
print(countryCodes)
// Prints "["BR": "Brazil", "JP": "Japan", "GH": "Ghana"]"
```

## Parameters

- `elements`: The key-value pairs that will make up the new   dictionary. Each key in   must be unique.

## See Also

- [var hashValue: Int](dictionary/hashvalue.md)
  The hash value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary/init(dictionaryliteral:))*