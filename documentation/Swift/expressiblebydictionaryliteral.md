# ExpressibleByDictionaryLiteral

**Framework**: Swift  
**Kind**: protocol

A type that can be initialized using a dictionary literal.

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
protocol ExpressibleByDictionaryLiteral
```

#### Overview

A dictionary literal is a simple way of writing a list of key-value pairs. You write each key-value pair with a colon (`:`) separating the key and the value. The dictionary literal is made up of one or more key-value pairs, separated by commas and surrounded with square brackets.

To declare a dictionary, assign a dictionary literal to a variable or constant:

```swift
let countryCodes = ["BR": "Brazil", "GH": "Ghana",
                    "JP": "Japan", "US": "United States"]
// 'countryCodes' has type '[String: String]'

print(countryCodes["BR"]!)
// Prints "Brazil"
```

When the context provides enough type information, you can use a special form of the dictionary literal, square brackets surrounding a single colon, to initialize an empty dictionary.

```swift
var frequencies: [String: Int] = [:]
print(frequencies.count)
// Prints "0"
```

> **Note**:  A dictionary literal is  the same as an instance of `Dictionary`. You can’t initialize a type that conforms to `ExpressibleByDictionaryLiteral` simply by assigning an instance of `Dictionary`, `KeyValuePairs`, or similar.

 A dictionary literal is  the same as an instance of `Dictionary`. You can’t initialize a type that conforms to `ExpressibleByDictionaryLiteral` simply by assigning an instance of `Dictionary`, `KeyValuePairs`, or similar.

### Conforming to the Expressiblebydictionaryliteral Protocol

To add the capability to be initialized with a dictionary literal to your own custom types, declare an `init(dictionaryLiteral:)` initializer. The following example shows the dictionary literal initializer for a hypothetical `CountedSet` type, which uses setlike semantics while keeping track of the count for duplicate elements:

```swift
struct CountedSet<Element: Hashable>: Collection, SetAlgebra {
    // implementation details

    /// Updates the count stored in the set for the given element,
    /// adding the element if necessary.
    ///
    /// - Parameter n: The new count for `element`. `n` must be greater
    ///   than or equal to zero.
    /// - Parameter element: The element to set the new count on.
    mutating func updateCount(_ n: Int, for element: Element)
}

extension CountedSet: ExpressibleByDictionaryLiteral {
    init(dictionaryLiteral elements: (Element, Int)...) {
        self.init()
        for (element, count) in elements {
            self.updateCount(count, for: element)
        }
    }
}
```

## Topics

### Associated Types
- [associatedtype Key](expressiblebydictionaryliteral/key.md)
  The key type of a dictionary literal.
- [associatedtype Value](expressiblebydictionaryliteral/value.md)
  The value type of a dictionary literal.
### Initializers
- [init(dictionaryLiteral: (Self.Key, Self.Value)...)](expressiblebydictionaryliteral/init(dictionaryliteral:).md)
  Creates an instance initialized with the given key-value pairs.

## Relationships

### Conforming Types
- [Dictionary](dictionary.md)
- [KeyValuePairs](keyvaluepairs.md)

## See Also

- [protocol ExpressibleByArrayLiteral](expressiblebyarrayliteral.md)
  A type that can be initialized using an array literal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/expressiblebydictionaryliteral)*