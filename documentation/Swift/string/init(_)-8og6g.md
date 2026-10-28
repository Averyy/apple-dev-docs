# init(_:)

**Framework**: Swift  
**Kind**: init  
**Role**: Initializer

Creates a new string containing the characters in the given sequence.

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
init<S>(_ characters: S) where S : Sequence, S.Element == Character
```

## Discussion

You can use this initializer to create a new string from the result of one or more collection operations on a string’s characters. For example:

```swift
let str = "The rain in Spain stays mainly in the plain."

let vowels: Set<Character> = ["a", "e", "i", "o", "u"]
let disemvoweled = String(str.lazy.filter { !vowels.contains($0) })

print(disemvoweled)
// Prints "Th rn n Spn stys mnly n th pln."
```

## Parameters

- `characters`: A string instance or another sequence of characters.

## See Also

### Creating a String
- [init(decoding: FilePath)](./init%28decoding%29-nm7v.md)
  Creates a string by interpreting the file path’s content as UTF-8 on Unix and UTF-16 on Windows.
- [init()](./init%28%29.md)
  Creates an empty string.
- [init(Character)](./init%28_%29-8v3fo.md)
  Creates a string containing the given character.
- [init<S>(S)](./init%28_%29-1ip93.md)
  Creates a new instance of a collection containing the elements of a sequence.
- [init<S>(S)](./init%28_%29-50pwi.md)
  Creates a new string containing the characters in the given sequence.
- [init(Substring)](./init%28_%29-14lv5.md)
  Creates a new string from the given substring.
- [init(repeating: String, count: Int)](./init%28repeating,count%29-23xjt.md)
  Creates a new string representing the given string repeated the specified number of times.
- [init(repeating: Character, count: Int)](./init%28repeating,count%29-11bpi.md)
  Creates a string representing the given character repeated the specified number of times.
- [init<E>(unsafeUninitializedCapacity: Int, initializingUTF8With: (UnsafeMutableBufferPointer<UInt8>) throws(E) -> Int) throws(E)](./init%28unsafeuninitializedcapacity,initializingutf8with%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/init(_:)-8og6g)*