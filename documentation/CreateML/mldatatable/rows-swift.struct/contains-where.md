# contains(where:)

**Framework**: Create ML  
**Kind**: method

Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func contains(where predicate: (Self.Element) throws -> Bool) rethrows -> Bool
```

#### Return Value

`true` if the sequence contains an element that satisfies `predicate`; otherwise, `false`.

#### Discussion

You can use the predicate to check for an element of a type that doesn’t conform to the `Equatable` protocol, such as the `HTTPResponse` enumeration in this example.

```None
enum HTTPResponse {
    case ok
    case error(Int)
}

let lastThreeResponses: [HTTPResponse] = [.ok, .ok, .error(404)]
let hadError = lastThreeResponses.contains { element in
    if case .error = element {
        return true
    } else {
        return false
    }
}
// 'hadError' == true
```

Alternatively, a predicate can be satisfied by a range of `Equatable` elements or a general condition. This example shows how you can check an array for an expense greater than $100.

```None
let expenses = [21.37, 55.21, 9.32, 10.18, 388.77, 11.41]
let hasBigPurchase = expenses.contains { $0 > 100 }
// 'hasBigPurchase' == true
```

> **Note**: O(), where  is the length of the sequence.

## Parameters

- `predicate`: A closure that takes an element of the sequence   as its argument and returns a Boolean value that indicates whether   the passed element represents a match.

## See Also

- [func contains(Self.Element) -> Bool](mldatatable/rows-swift.struct/contains(_:).md)
  Returns a Boolean value indicating whether the sequence contains the given element.
- [func allSatisfy((Self.Element) throws -> Bool) rethrows -> Bool](mldatatable/rows-swift.struct/allsatisfy(_:).md)
  Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [func first(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](mldatatable/rows-swift.struct/first(where:).md)
  Returns the first element of the sequence that satisfies the given predicate.
- [func firstIndex(of: Self.Element) -> Self.Index?](mldatatable/rows-swift.struct/firstindex(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](mldatatable/rows-swift.struct/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func last(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](mldatatable/rows-swift.struct/last(where:).md)
  Returns the last element of the sequence that satisfies the given predicate.
- [func lastIndex(of: Self.Element) -> Self.Index?](mldatatable/rows-swift.struct/lastindex(of:).md)
  Returns the last index where the specified value appears in the collection.
- [func lastIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](mldatatable/rows-swift.struct/lastindex(where:).md)
  Returns the index of the last element in the collection that matches the given predicate.
- [func min(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](mldatatable/rows-swift.struct/min(by:).md)
  Returns the minimum element in the sequence, using the given predicate as the comparison between elements.
- [func max(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](mldatatable/rows-swift.struct/max(by:).md)
  Returns the maximum element in the sequence, using the given predicate as the comparison between elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/rows-swift.struct/contains(where:))*