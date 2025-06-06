# remove(_:)

**Framework**: RealityKit  
**Kind**: method

Removes the given element and all elements subsumed by it.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
@discardableResult
mutating func remove(_ member: Self.Element) -> Self.Element?
```

#### Return Value

The intersection of `[member]` and the set, if the intersection was nonempty; otherwise, `nil`.

#### Discussion

In the following example, the `.priority` shipping option is removed from the `options` option set. Attempting to remove the same shipping option a second time results in `nil`, because `options` no longer contains `.priority` as a member.

```None
var options: ShippingOptions = [.secondDay, .priority]
let priorityOption = options.remove(.priority)
print(priorityOption == .priority)
// Prints "true"

print(options.remove(.priority))
// Prints "nil"
```

In the next example, the `.express` element is passed to `remove(_:)`. Although `.express` is not a member of `options`, `.express` subsumes the remaining `.secondDay` element of the option set. Therefore, `options` is emptied and the intersection between `.express` and `options` is returned.

```None
let expressOption = options.remove(.express)
print(expressOption == .express)
// Prints "false"
print(expressOption == .secondDay)
// Prints "true"
```

## Parameters

- `member`: The element of the set to remove.

## See Also

- [func insert(Self.Element) -> (inserted: Bool, memberAfterInsert: Self.Element)](arview/debugoptions-swift.struct/insert(_:).md)
  Adds the given element to the option set if it is not already a member.
- [func update(with: Self.Element) -> Self.Element?](arview/debugoptions-swift.struct/update(with:).md)
  Inserts the given element into the set.
- [func subtract(Self)](arview/debugoptions-swift.struct/subtract(_:).md)
  Removes the elements of the given set from this set.
- [func subtracting(Self) -> Self](arview/debugoptions-swift.struct/subtracting(_:).md)
  Returns a new set containing the elements of this set that do not occur in the given set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/debugoptions-swift.struct/remove(_:))*