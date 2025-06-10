# JSONEncoder.KeyEncodingStrategy.custom(_:)

**Framework**: Foundation  
**Kind**: case

A key encoding strategy defined by the closure you supply.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@preconcurrency
case custom(([any CodingKey]) -> any CodingKey)
```

#### Discussion

The value associated with this case is a closure you use to choose the names of keys in the encoded JSON object. During encoding, the closure executes once for each key in the [`Encodable`](https://developer.apple.com/documentation/Swift/Encodable) value. The closure receives an array of [`CodingKey`](https://developer.apple.com/documentation/Swift/CodingKey) instances representing the sequence of keys needed to reach the value the encoder is currently encoding.

The example below shows how to encode the properties of the nested `A`, `B`, and `C` structures with custom logic that you specify in the closure value associated with the custom case.

```swift
struct A: Codable {
    var value: Int
    var b: B
    
    struct B: Codable {
        var value: Int
        var c: C
        
        struct C: Codable {
            var value: Int
        }
    }
}

let a: A = A(value: 1, b: .init(value: 2, c: .init(value: 3)))

print(a.b.c.value) // Prints "3"

let encoder = JSONEncoder()
encoder.outputFormatting = [.prettyPrinted, .sortedKeys]
let encodeAndPrint = { print(String(data: try encoder.encode(a), encoding: .utf8) ?? "String encoding error.") }

/// An implementation of CodingKey that's useful for combining and transforming keys as strings.
struct AnyKey: CodingKey {
    var stringValue: String
    var intValue: Int?
    
    init?(stringValue: String) {
        self.stringValue = stringValue
        self.intValue = nil
    }
    
    init?(intValue: Int) {
        self.stringValue = String(intValue)
        self.intValue = intValue
    }
}
```

In the next example, you use the `AnyKey` structure defined above to customize the encoding of the `A`, `B`, and `C` structures.

```swift
// Customize each `value` key to contain a dot-syntax path.
encoder.keyEncodingStrategy = .custom { keys in
    if keys.last!.stringValue == "value" {
        return AnyKey(stringValue: "a." + keys.map { key in
            key.stringValue
        }.joined(separator: "."))!
    } else {
        return keys.last!
    }
}

try encodeAndPrint()
```

Here’s the JSON object that results from the custom encoding above:

```javascript
 {
     "a.value": 1,
     "b": {
         "a.b.value": 2,
         "c": {
            "a.b.c.value": 3
         }
     }
 }
```

## Parameters

- `codingPath`: A closure that provides the full path to the current encoding position, and returns a customized coding key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/jsonencoder/keyencodingstrategy-swift.enum/custom(_:))*