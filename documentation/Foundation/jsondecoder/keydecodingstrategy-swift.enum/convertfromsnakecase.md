# JSONDecoder.KeyDecodingStrategy.convertFromSnakeCase

**Framework**: Foundation  
**Kind**: case

A key decoding strategy that converts snake-case keys to camel-case keys.

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
case convertFromSnakeCase
```

#### Discussion

Snake-case and camel-case are two common approaches for combining words when naming parts of an API. The Swift [`API Design Guidelines`](https://developer.apple.comhttps://swift.org/documentation/api-design-guidelines/#general-conventions) recommend using camel-case names. Some JSON APIs adopt snake-case; use this strategy when you encounter such an API.

This strategy uses [`uppercaseLetters`](characterset/uppercaseletters.md) and [`lowercaseLetters`](characterset/lowercaseletters.md) to determine the boundaries between words, and the [`system`](nslocale/system.md) locale when capitalizing letters.

This strategy follows these steps to convert JSON keys to camel-case:

1. Capitalize each word that follows an underscore.
2. Remove all underscores that aren’t at the very start or end of the string.
3. Combine the words into a single string.

The following examples show the result of applying this strategy:

> **Note**:  The [`JSONDecoder.KeyDecodingStrategy.convertFromSnakeCase`](jsondecoder/keydecodingstrategy-swift.enum/convertfromsnakecase.md) strategy can’t infer capitalization for acronyms or initialisms such as WYSIWYG or URI. The example above shows how the automatic conversion differs from the conversion you might expect: `baseURI`. To decode such a key with the correct capitalization, define a custom `CodingKeys` enumeration, as described in [`Encoding and Decoding Custom Types`](encoding-and-decoding-custom-types.md).

The example below shows how properties on the `OlympicEventResult` structure convert from snake-case when decoded as keys in a JSON object.

```swift
struct OlympicEventResult: Codable {
    var goldWinner: String
    var silverWinner: String
    var bronzeWinner: String
}

let json = """
{
    "silver_winner": "Sound",
    "gold_winner": "Light",
    "bronze_winner": "Unladen Swallow"
}
""".data(using: .utf8)!

let decoder = JSONDecoder()
let decodeAndPrint = { print(try! decoder.decode(OlympicEventResult.self, from: json)) }

decoder.keyDecodingStrategy = .convertFromSnakeCase
decodeAndPrint()

// Prints: "OlympicEventResult(goldWinner: "Light", silverWinner: "Sound", bronzeWinner: "Unladen Swallow")"
```

## See Also

- [JSONEncoder.KeyEncodingStrategy.convertToSnakeCase](jsonencoder/keyencodingstrategy-swift.enum/converttosnakecase.md)
  A key encoding strategy that converts camel-case keys to snake-case keys.
- [JSONDecoder.KeyDecodingStrategy.useDefaultKeys](jsondecoder/keydecodingstrategy-swift.enum/usedefaultkeys.md)
  A key decoding strategy that doesn’t change key names during decoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/jsondecoder/keydecodingstrategy-swift.enum/convertfromsnakecase)*