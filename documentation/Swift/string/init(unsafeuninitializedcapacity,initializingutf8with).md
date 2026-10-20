# init(unsafeUninitializedCapacity:initializingUTF8With:)

**Framework**: Swift  
**Kind**: init  
**Role**: Initializer

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
init<E>(unsafeUninitializedCapacity capacity: Int, initializingUTF8With initializer: (UnsafeMutableBufferPointer<UInt8>) throws(E) -> Int) throws(E) where E : Error
```

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
- [init(repeating: Character, count: Int)](./init%28repeating,count%29-11bpi.md)
  Creates a string representing the given character repeated the specified number of times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/init(unsafeuninitializedcapacity:initializingutf8with:))*