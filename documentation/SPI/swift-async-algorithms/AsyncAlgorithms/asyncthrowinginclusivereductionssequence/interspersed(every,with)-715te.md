---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncthrowinginclusivereductionssequence/interspersed(every:with:)-715te"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# interspersed(every:with:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Returns a new asynchronous sequence containing the elements of this asynchronous sequence, inserting the given separator between each element.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
func interspersed(every: Int = 1, with separator: @escaping @Sendable () async throws -> Self.Element) -> AsyncThrowingInterspersedSequence<Self>
```

## Return Value

The interspersed asynchronous sequence of elements.

## Discussion

Any value of this asynchronous sequence’s element type can be used as the separator.

The following example shows how an async sequences of `String`s can be interspersed using `-` as the separator:

```
let input = ["A", "B", "C"].async
let interspersed = input.interspersed(with: { "-" })
for await element in interspersed {
  print(element)
}
// Prints "A" "-" "B" "-" "C"
```

## Parameters

- `every`: Dictates after how many elements a separator should be inserted.
- `separator`: A closure that produces the value to insert in between each of this async sequence’s elements.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncthrowinginclusivereductionssequence/interspersed(every:with:)-715te)*