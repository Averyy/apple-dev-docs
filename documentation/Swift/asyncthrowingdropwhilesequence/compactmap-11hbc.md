# compactMap(_:)

**Framework**: Swift  
**Kind**: method

Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements, omitting results that don’t return a value.

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
@preconcurrency
func compactMap<ElementOfResult>(_ transform: @escaping (Self.Element) async -> ElementOfResult?) -> AsyncCompactMapSequence<Self, ElementOfResult>
```

#### Return Value

An asynchronous sequence that contains, in order, the non-`nil` elements produced by the `transform` closure.

#### Discussion

Use the `compactMap(_:)` method to transform every element received from a base asynchronous sequence, while also discarding any `nil` results from the closure. Typically, you use this to transform from one type of element to another.

In this example, an asynchronous sequence called `Counter` produces `Int` values from `1` to `5`. The closure provided to the `compactMap(_:)` method takes each `Int` and looks up a corresponding `String` from a `romanNumeralDict` dictionary. Because there is no key for `4`, the closure returns `nil` in this case, which `compactMap(_:)` omits from the transformed asynchronous sequence.

```swift
let romanNumeralDict: [Int: String] =
    [1: "I", 2: "II", 3: "III", 5: "V"]
    
let stream = Counter(howHigh: 5)
    .compactMap { romanNumeralDict[$0] }
for await numeral in stream {
    print(numeral, terminator: " ")
}
// Prints "I II III V "
```

## Parameters

- `transform`: A mapping closure.   accepts an element   of this sequence as its parameter and returns a transformed value of the   same or of a different type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncthrowingdropwhilesequence/compactmap(_:)-11hbc)*