# map(_:)

**Framework**: Combine  
**Kind**: method

Creates an asynchronous sequence that maps the given error-throwing closure over the asynchronous sequence’s elements.

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
func map<Transformed>(_ transform: @escaping (Self.Element) async throws -> Transformed) -> AsyncThrowingMapSequence<Self, Transformed>
```

#### Return Value

An asynchronous sequence that contains, in order, the elements produced by the `transform` closure.

#### Discussion

Use the `map(_:)` method to transform every element received from a base asynchronous sequence. Typically, you use this to transform from one type of element to another.

In this example, an asynchronous sequence called `Counter` produces `Int` values from `1` to `5`. The closure provided to the `map(_:)` method takes each `Int` and looks up a corresponding `String` from a `romanNumeralDict` dictionary. This means the outer `for await in` loop iterates over `String` instances instead of the underlying `Int` values that `Counter` produces. Also, the dictionary doesn’t provide a key for `4`, and the closure throws an error for any key it can’t look up, so receiving this value from `Counter` ends the modified sequence with an error.

```swift
let romanNumeralDict: [Int: String] =
    [1: "I", 2: "II", 3: "III", 5: "V"]

do {
    let stream = Counter(howHigh: 5)
        .map { (value) throws -> String in
            guard let roman = romanNumeralDict[value] else {
                throw MyError()
            }
            return roman
        }
    for try await numeral in stream {
        print(numeral, terminator: " ")
    }
} catch {
    print("Error: \(error)")
}
// Prints "I II III Error: MyError() "
```

## Parameters

- `transform`: A mapping closure.   accepts an element   of this sequence as its parameter and returns a transformed value of the   same or of a different type.   can also throw an error, which   ends the transformed sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/asyncthrowingpublisher/map(_:)-5vt13)*