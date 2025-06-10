# encode(encoder:)

**Framework**: Swift  
**Kind**: method

Encodes the output from upstream using a specified encoder.

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
func encode<Coder>(encoder: Coder) -> Publishers.Encode<Self, Coder> where Coder : TopLevelEncoder
```

#### Return Value

A publisher that encodes received elements using a specified encoder, and publishes the resulting data.

#### Discussion

Use [`encode(encoder:)`](optional/publisher-swift.struct/encode(encoder:).md) with a [`JSONDecoder`](https://developer.apple.com/documentation/Foundation/JSONDecoder) (or a [`PropertyListDecoder`](https://developer.apple.com/documentation/Foundation/PropertyListDecoder) for property lists) to encode an [`Encodable`](Encodable.md) struct into [`Data`](https://developer.apple.com/documentation/Foundation/Data) that could be used to make a JSON string (or written to disk as a binary plist in the case of property lists).

In this example, a `PassthroughSubject` publishes an `Article`. The [`encode(encoder:)`](optional/publisher-swift.struct/encode(encoder:).md) operator encodes the properties of the `Article` struct into a new JSON string according to the [`Codable`](Codable.md) protocol adopted by `Article`. The operator publishes the resulting JSON string to the downstream subscriber. If the encoding operation fails, which can happen in the case of complex properties that can’t be directly transformed into JSON, the stream terminates and the error is passed to the downstream subscriber.

```swift
struct Article: Codable {
    let title: String
    let author: String
    let pubDate: Date
}

let dataProvider = PassthroughSubject<Article, Never>()
let cancellable = dataProvider
    .encode(encoder: JSONEncoder())
    .sink(receiveCompletion: { print ("Completion: \($0)") },
          receiveValue: {  data in
            guard let stringRepresentation = String(data: data, encoding: .utf8) else { return }
            print("Data received \(data) string representation: \(stringRepresentation)")
    })

dataProvider.send(Article(title: "My First Article", author: "Gita Kumar", pubDate: Date()))

// Prints: "Data received 86 bytes string representation: {"title":"My First Article","author":"Gita Kumar","pubDate":606211803.279603}"
```

## Parameters

- `encoder`: An encoder that implements the   protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/optional/publisher-swift.struct/encode(encoder:))*