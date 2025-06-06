# subscript(_:default:)

**Framework**: Swift  
**Kind**: subscript

Accesses the value with the given key, falling back to the given default value if the key isn’t found.

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
subscript(key: Key, default defaultValue: @autoclosure () -> Value) -> Value { get set }
```

#### Return Value

The value associated with `key` in the dictionary; otherwise, `defaultValue`.

#### Overview

Use this subscript when you want either the value for a particular key or, when that key is not present in the dictionary, a default value. This example uses the subscript with a message to use in case an HTTP response code isn’t recognized:

```swift
var responseMessages = [200: "OK",
                        403: "Access forbidden",
                        404: "File not found",
                        500: "Internal server error"]

let httpResponseCodes = [200, 403, 301]
for code in httpResponseCodes {
    let message = responseMessages[code, default: "Unknown response"]
    print("Response \(code): \(message)")
}
// Prints "Response 200: OK"
// Prints "Response 403: Access forbidden"
// Prints "Response 301: Unknown response"
```

When a dictionary’s `Value` type has value semantics, you can use this subscript to perform in-place operations on values in the dictionary. The following example uses this subscript while counting the occurrences of each letter in a string:

```swift
let message = "Hello, Elle!"
var letterCounts: [Character: Int] = [:]
for letter in message {
    letterCounts[letter, default: 0] += 1
}
// letterCounts == ["H": 1, "e": 2, "l": 4, "o": 1, ...]
```

When `letterCounts[letter, default: 0] += 1` is executed with a value of `letter` that isn’t already a key in `letterCounts`, the specified default value (`0`) is returned from the subscript, incremented, and then added to the dictionary under that key.

> **Note**: Do not use this subscript to modify dictionary values if the dictionary’s `Value` type is a class. In that case, the default value and key are not written back to the dictionary after an operation.

Do not use this subscript to modify dictionary values if the dictionary’s `Value` type is a class. In that case, the default value and key are not written back to the dictionary after an operation.

## Parameters

- `key`: The key the look up in the dictionary.
- `defaultValue`: The default value to use if   doesn’t exist in the   dictionary.

## See Also

- [subscript(Key) -> Value?](dictionary/subscript(_:)-8rfql.md)
  Accesses the value associated with the given key for reading and writing.
- [func index(forKey: Key) -> Dictionary<Key, Value>.Index?](dictionary/index(forkey:).md)
  Returns the index for the given key.
- [subscript(Dictionary<Key, Value>.Index) -> Dictionary<Key, Value>.Element](dictionary/subscript(_:)-4bhoo.md)
  Accesses the key-value pair at the specified position.
- [var keys: Dictionary<Key, Value>.Keys](dictionary/keys-swift.property.md)
  A collection containing just the keys of the dictionary.
- [var values: Dictionary<Key, Value>.Values](dictionary/values-swift.property.md)
  A collection containing just the values of the dictionary.
- [var first: Self.Element?](dictionary/first.md)
  The first element of the collection.
- [func randomElement() -> Self.Element?](dictionary/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](dictionary/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary/subscript(_:default:))*