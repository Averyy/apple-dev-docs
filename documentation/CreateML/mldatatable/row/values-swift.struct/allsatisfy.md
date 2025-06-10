# allSatisfy(_:)

**Framework**: Create ML  
**Kind**: method

Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

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

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/row/values-swift.struct/allsatisfy(_:))*