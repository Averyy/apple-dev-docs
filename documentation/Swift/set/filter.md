# filter(_:)

**Framework**: Swift  
**Kind**: method

Returns a new set containing the elements of the set that satisfy the given predicate.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+
- Swift 4.0+

## Declaration

```swift
func filter(_ isIncluded: (Element) throws -> Bool) rethrows -> Set<Element>
```

#### Return Value

A set of the elements that `isIncluded` allows.

#### Discussion

In this example, `filter(_:)` is used to include only names shorter than five characters.

```swift
let cast: Set = ["Vivien", "Marlon", "Kim", "Karl"]
let shortNames = cast.filter { $0.count < 5 }

shortNames.isSubset(of: cast)
// true
shortNames.contains("Vivien")
// false
```

## Parameters

- `isIncluded`: A closure that takes an element as its argument   and returns a Boolean value indicating whether the element should be   included in the returned set.

## See Also

- [func remove(Element) -> Element?](set/remove(_:)-8p2tv.md)
  Removes the specified element from the set.
- [func remove<ConcreteElement>(ConcreteElement) -> ConcreteElement?](set/remove(_:)-4d3i1.md)
- [func removeFirst() -> Element](set/removefirst.md)
  Removes the first element of the set.
- [func remove(at: Set<Element>.Index) -> Element](set/remove(at:).md)
  Removes the element at the given index of the set.
- [func removeAll(keepingCapacity: Bool)](set/removeall(keepingcapacity:).md)
  Removes all members from the set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/set/filter(_:))*