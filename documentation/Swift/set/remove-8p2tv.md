# remove(_:)

**Framework**: Swift  
**Kind**: method

Removes the specified element from the set.

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
@discardableResult
mutating func remove(_ member: Element) -> Element?
```

#### Return Value

The value of the `member` parameter if it was a member of the set; otherwise, `nil`.

#### Discussion

This example removes the element `"sugar"` from a set of ingredients.

```swift
var ingredients: Set = ["cocoa beans", "sugar", "cocoa butter", "salt"]
let toRemove = "sugar"
if let removed = ingredients.remove(toRemove) {
    print("The recipe is now \(removed)-free.")
}
// Prints "The recipe is now sugar-free."
```

## Parameters

- `member`: The element to remove from the set.

## See Also

- [func filter((Element) throws -> Bool) rethrows -> Set<Element>](set/filter(_:).md)
  Returns a new set containing the elements of the set that satisfy the given predicate.
- [func remove<ConcreteElement>(ConcreteElement) -> ConcreteElement?](set/remove(_:)-4d3i1.md)
- [func removeFirst() -> Element](set/removefirst.md)
  Removes the first element of the set.
- [func remove(at: Set<Element>.Index) -> Element](set/remove(at:).md)
  Removes the element at the given index of the set.
- [func removeAll(keepingCapacity: Bool)](set/removeall(keepingcapacity:).md)
  Removes all members from the set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/set/remove(_:)-8p2tv)*