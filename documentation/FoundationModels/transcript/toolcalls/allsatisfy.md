# allSatisfy(_:)

**Framework**: Foundation Models  
**Kind**: method

Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func allSatisfy(_ predicate: (Self.Element) throws -> Bool) rethrows -> Bool
```

#### Return Value

`true` if the sequence contains only elements that satisfy `predicate`; otherwise, `false`.

#### Discussion

The following code uses this method to test whether all the names in an array have at least five characters:

```None
let names = ["Sofia", "Camilla", "Martina", "Mateo", "Nicolás"]
let allHaveAtLeastFive = names.allSatisfy({ $0.count >= 5 })
// allHaveAtLeastFive == true
```

If the sequence is empty, this method returns `true`.

> **Note**: O(), where  is the length of the sequence.

## Parameters

- `predicate`: A closure that takes an element of the sequence   as its argument and returns a Boolean value that indicates whether   the passed element satisfies a condition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/toolcalls/allsatisfy(_:))*