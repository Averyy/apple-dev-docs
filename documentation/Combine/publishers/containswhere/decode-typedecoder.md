# decode(type:decoder:)

**Framework**: Combine  
**Kind**: method

Decodes the output from the upstream using a specified decoder.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func decode<Item, Coder>(type: Item.Type, decoder: Coder) -> Publishers.Decode<Self, Item, Coder> where Item : Decodable, Coder : TopLevelDecoder, Self.Output == Coder.Input
```

#### Return Value

A publisher that decodes a given type using a specified decoder and publishes the result.

#### Discussion

Use [`decode(type:decoder:)`](publisher/decode(type:decoder:).md) with a [`JSONDecoder`](https://developer.apple.com/documentation/Foundation/JSONDecoder) (or a [`PropertyListDecoder`](https://developer.apple.com/documentation/Foundation/PropertyListDecoder) for property lists) to decode data received from a [`URLSession.DataTaskPublisher`](https://developer.apple.com/documentation/Foundation/URLSession/DataTaskPublisher) or other data source using the [`Decodable`](https://developer.apple.com/documentation/Swift/Decodable) protocol.

In this example, a [`PassthroughSubject`](passthroughsubject.md) publishes a JSON string. The JSON decoder parses the string, converting its fields according to the [`Decodable`](https://developer.apple.com/documentation/Swift/Decodable) protocol implemented by `Article`, and successfully populating a new `Article`. The [`Publishers.Decode`](publishers/decode.md) publisher then publishes the `Article` to the downstream. If a decoding operation fails, which happens in the case of missing or malformed data in the source JSON string, the stream terminates and passes the error to the downstream subscriber.

```swift
struct Article: Codable {
    let title: String
    let author: String
    let pubDate: Date
}

let dataProvider = PassthroughSubject<Data, Never>()
cancellable = dataProvider
    .decode(type: Article.self, decoder: JSONDecoder())
    .sink(receiveCompletion: { print ("Completion: \($0)")},
          receiveValue: { print ("value: \($0)") })

dataProvider.send(Data("{\"pubDate\":1574273638.575666, \"title\" : \"My First Article\", \"author\" : \"Gita Kumar\" }".utf8))

// Prints: ".sink() data received Article(title: "My First Article", author: "Gita Kumar", pubDate: 2050-11-20 18:13:58 +0000)"
```

## Parameters

- `type`: The encoded data to decode into a struct that conforms to the   protocol.
- `decoder`: A decoder that implements the   protocol.

## See Also

- [func encode<Coder>(encoder: Coder) -> Publishers.Encode<Self, Coder>](publishers/containswhere/encode(encoder:).md)
  Encodes the output from upstream using a specified encoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/containswhere/decode(type:decoder:))*