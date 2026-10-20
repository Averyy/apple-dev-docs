# init(repeating:count:)

**Framework**: Swift  
**Kind**: init  
**Role**: Initializer

Creates a string representing the given character repeated the specified number of times.

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
init(repeating repeatedValue: Character, count: Int)
```

#### Discussion

For example, use this initializer to create a string with ten `"0"` characters in a row.

```swift
let zeroes = String(repeating: "0" as Character, count: 10)
print(zeroes)
// Prints "0000000000"
```

## Parameters

- `repeatedValue`: The character to repeat.
- `count`: The number of times to repeat `repeatedValue` in the resulting string.

## See Also

### Creating a String
- [init(decoding: FilePath)](./init%28decoding%29-nm7v.md)
  Creates a string by interpreting the file path’s content as UTF-8 on Unix and UTF-16 on Windows.
- [init()](./init%28%29.md)
  Creates an empty string.
- [init(Character)](./init%28_%29-8v3fo.md)
  Creates a string containing the given character.
- [init<S>(S)](./init%28_%29-8og6g.md)
  Creates a new string containing the characters in the given sequence.
- [init<S>(S)](./init%28_%29-1ip93.md)
  Creates a new instance of a collection containing the elements of a sequence.
- [init<S>(S)](./init%28_%29-50pwi.md)
  Creates a new string containing the characters in the given sequence.
- [init(Substring)](./init%28_%29-14lv5.md)
  Creates a new string from the given substring.
- [init(repeating: String, count: Int)](./init%28repeating,count%29-23xjt.md)
  Creates a new string representing the given string repeated the specified number of times.
- [init<E>(unsafeUninitializedCapacity: Int, initializingUTF8With: (UnsafeMutableBufferPointer<UInt8>) throws(E) -> Int) throws(E)](./init%28unsafeuninitializedcapacity,initializingutf8with%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/init(repeating:count:)-11bpi)*