# contains(where:)

**Framework**: Foundation Models  
**Kind**: method

Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/toolcalls/contains(where:))*