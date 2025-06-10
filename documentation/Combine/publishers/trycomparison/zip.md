# zip(_:_:_:_:)

**Framework**: Combine  
**Kind**: method

Combines elements from three other publishers and delivers a transformed output.

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
func zip<P, Q, R, T>(_ publisher1: P, _ publisher2: Q, _ publisher3: R, _ transform: @escaping (Self.Output, P.Output, Q.Output, R.Output) -> T) -> Publishers.Map<Publishers.Zip4<Self, P, Q, R>, T> where P : Publisher, Q : Publisher, R : Publisher, Self.Failure == P.Failure, P.Failure == Q.Failure, Q.Failure == R.Failure
```

#### Return Value

A publisher that uses the `transform` closure to emit new elements, produced by combining the most recent value from four upstream publishers.

#### Discussion

Use [`zip(_:_:_:_:)`](publisher/zip(_:_:_:_:).md) to return a new publisher that combines the elements from three other publishers using a transformation you specify to publish a new value to the downstream subscriber. The returned publisher waits until all four publishers have emitted an event, then delivers the oldest unconsumed event from each publisher together that the operator uses in the transformation.

In this example, the [`PassthroughSubject`](passthroughsubject.md) publishers, `numbersPub`, `fractionsPub`, `lettersPub`, and `emojiPub` emit values. The [`zip(_:_:_:_:)`](publisher/zip(_:_:_:_:).md) operator receives the oldest value from each publisher and uses the `Int` from `numbersPub` and publishes a string that repeats the [`String`](https://developer.apple.com/documentation/Swift/String) from `lettersPub` and `emojiPub` that many times and prints out the value in `fractionsPub`.

```swift
let numbersPub = PassthroughSubject<Int, Never>()      // first publisher
let lettersPub = PassthroughSubject<String, Never>()   // second
let emojiPub = PassthroughSubject<String, Never>()     // third
let fractionsPub  = PassthroughSubject<Double, Never>()// fourth

cancellable = numbersPub
    .zip(lettersPub, emojiPub, fractionsPub) { anInt, aLetter, anEmoji, aFraction  in
        ("\(String(repeating: anEmoji, count: anInt)) \(String(repeating: aLetter, count: anInt)) \(aFraction)")
    }
    .sink { print("\($0)") }

numbersPub.send(1)         // numbersPub: 1       lettersPub:          emojiPub:          zip output: <none>
numbersPub.send(2)         // numbersPub: 1,2     lettersPub:          emojiPub:          zip output: <none>
numbersPub.send(3)         // numbersPub: 1,2,3   lettersPub:          emojiPub:          zip output: <none>
fractionsPub.send(0.1)     // numbersPub: 1,2,3   lettersPub: "A"      emojiPub:          zip output: <none>
lettersPub.send("A")       // numbersPub: 1,2,3   lettersPub: "A"      emojiPub:          zip output: <none>
emojiPub.send("😀")        // numbersPub: 1,2,3   lettersPub: "A"      emojiPub:"😀"      zip output: "😀 A"
lettersPub.send("B")       // numbersPub: 2,3     lettersPub: "B"      emojiPub:          zip output: <none>
fractionsPub.send(0.8)     // numbersPub: 2,3     lettersPub: "A"      emojiPub:          zip output: <none>
emojiPub.send("🥰")        // numbersPub: 3       lettersPub: "B"      emojiPub:          zip output: "🥰🥰 BB"
// Prints:
//1 😀 A 0.1
//2 🥰🥰 BB 0.8
```

If any upstream publisher finishes successfully or fails with an error, so too does the zipped publisher.

## Parameters

- `publisher1`: A second publisher.
- `publisher2`: A third publisher.
- `publisher3`: A fourth publisher.
- `transform`: A closure that receives the most-recent value from each publisher and returns a new value to publish.

## See Also

- [func zip<P>(P) -> Publishers.Zip<Self, P>](publishers/trycomparison/zip(_:).md)
  Combines elements from another publisher and deliver pairs of elements as tuples.
- [func zip<P, T>(P, (Self.Output, P.Output) -> T) -> Publishers.Map<Publishers.Zip<Self, P>, T>](publishers/trycomparison/zip(_:_:)-37xdn.md)
  Combines elements from another publisher and delivers a transformed output.
- [func zip<P, Q>(P, Q) -> Publishers.Zip3<Self, P, Q>](publishers/trycomparison/zip(_:_:)-li3l.md)
  Combines elements from two other publishers and delivers groups of elements as tuples.
- [func zip<P, Q, T>(P, Q, (Self.Output, P.Output, Q.Output) -> T) -> Publishers.Map<Publishers.Zip3<Self, P, Q>, T>](publishers/trycomparison/zip(_:_:_:)-24tg9.md)
  Combines elements from two other publishers and delivers a transformed output.
- [func zip<P, Q, R>(P, Q, R) -> Publishers.Zip4<Self, P, Q, R>](publishers/trycomparison/zip(_:_:_:)-2pyua.md)
  Combines elements from three other publishers and delivers groups of elements as tuples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/trycomparison/zip(_:_:_:_:))*