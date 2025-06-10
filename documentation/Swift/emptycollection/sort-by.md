# sort(by:)

**Framework**: Swift  
**Kind**: method

Sorts the collection in place, using the given predicate as the comparison between elements.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
mutating func sort(by areInIncreasingOrder: (Self.Element, Self.Element) throws -> Bool) rethrows
```

#### Discussion

When you want to sort a collection of elements that don’t conform to the `Comparable` protocol, pass a closure to this method that returns `true` when the first element should be ordered before the second.

In the following example, the closure provides an ordering for an array of a custom enumeration that describes an HTTP response. The predicate orders errors before successes and sorts the error responses by their error code.

```swift
enum HTTPResponse {
    case ok
    case error(Int)
}

var responses: [HTTPResponse] = [.error(500), .ok, .ok, .error(404), .error(403)]
responses.sort {
    switch ($0, $1) {
    // Order errors by code
    case let (.error(aCode), .error(bCode)):
        return aCode < bCode

    // All successes are equivalent, so none is before any other
    case (.ok, .ok): return false

    // Order errors before successes
    case (.error, .ok): return true
    case (.ok, .error): return false
    }
}
print(responses)
// Prints "[.error(403), .error(404), .error(500), .ok, .ok]"
```

Alternatively, use this method to sort a collection of elements that do conform to `Comparable` when you want the sort to be descending instead of ascending. Pass the greater-than operator (`>`) operator as the predicate.

```swift
var students = ["Kofi", "Abena", "Peter", "Kweku", "Akosua"]
students.sort(by: >)
print(students)
// Prints "["Peter", "Kweku", "Kofi", "Akosua", "Abena"]"
```

`areInIncreasingOrder` must be a  over the elements. That is, for any elements `a`, `b`, and `c`, the following conditions must hold:

- `areInIncreasingOrder(a, a)` is always `false`. (Irreflexivity)
- If `areInIncreasingOrder(a, b)` and `areInIncreasingOrder(b, c)` are both `true`, then `areInIncreasingOrder(a, c)` is also `true`. (Transitive comparability)
- Two elements are  if neither is ordered before the other according to the predicate. If `a` and `b` are incomparable, and `b` and `c` are incomparable, then `a` and `c` are also incomparable. (Transitive incomparability)

The sorting algorithm is guaranteed to be stable. A stable sort preserves the relative order of elements for which `areInIncreasingOrder` does not establish an order.

> **Note**: O( log ), where  is the length of the collection.

## Parameters

- `areInIncreasingOrder`: A predicate that returns   if its   first argument should be ordered before its second argument;   otherwise,  . If   throws an error during   the sort, the elements may be in a different order, but none will be   lost.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/emptycollection/sort(by:))*