# JSONDecoder.KeyDecodingStrategy.custom(_:)

**Framework**: Foundation  
**Kind**: case

A key decoding strategy defined by the closure you supply.

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

The value associated with this case is a closure you use to map names of keys from the decoded JSON object to the names of your type’s coding keys. During decoding, the closure executes once for each key in the [`Decodable`](https://developer.apple.com/documentation/Swift/Decodable) value. When called, the closure receives an array of [`CodingKey`](https://developer.apple.com/documentation/Swift/CodingKey) instances representing the sequence of keys needed to reach the value the decoder is currently decoding.

The example below shows how to decode the properties of the nested `A`, `B`, and `C` structures with custom logic that you specify in the closure value associated with the custom case.

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

let json = """
{
    "a.value": 1,
    "b": {
        "a.b.value": 2,
        "c": {
            "a.b.c.value": 3
        }
    }
}
""".data(using: .utf8)!

let decoder = JSONDecoder()

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

In the next example you use the `AnyKey` structure defined above to customize the decoding of the `A`, `B`, and `C` structures.

```swift
// Customize each key to remove any preceding, dot-syntax paths.
decoder.keyDecodingStrategy = .custom { keys in
    let lastComponent = keys.last!.stringValue.split(separator: ".").last!
    return AnyKey(stringValue: String(lastComponent))!
}

let a = try decoder.decode(A.self, from: json)

print(a.b.c.value) // Prints "3"
```

## Parameters

- `codingPath`: A closure that receives as a parameter an array of CodingKey instances representing the sequence of keys needed to reach the value the decoder is currently decoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/jsondecoder/keydecodingstrategy-swift.enum/custom(_:))*