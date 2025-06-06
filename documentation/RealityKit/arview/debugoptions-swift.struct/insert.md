# insert(_:)

**Framework**: RealityKit  
**Kind**: method

Adds the given element to the option set if it is not already a member.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
@discardableResult
mutating func insert(_ newMember: Self.Element) -> (inserted: Bool, memberAfterInsert: Self.Element)
```

#### Return Value

`(true, newMember)` if `newMember` was not contained in `self`. Otherwise, returns `(false, oldMember)`, where `oldMember` is the member of the set equal to `newMember`.

#### Discussion

In the following example, the `.secondDay` shipping option is added to the `freeOptions` option set if `purchasePrice` is greater than 50.0. For the `ShippingOptions` declaration, see the `OptionSet` protocol discussion.

```None
let purchasePrice = 87.55

var freeOptions: ShippingOptions = [.standard, .priority]
if purchasePrice > 50 {
    freeOptions.insert(.secondDay)
}
print(freeOptions.contains(.secondDay))
// Prints "true"
```

## Parameters

- `newMember`: The element to insert.

## See Also

- [func update(with: Self.Element) -> Self.Element?](arview/debugoptions-swift.struct/update(with:).md)
  Inserts the given element into the set.
- [func remove(Self.Element) -> Self.Element?](arview/debugoptions-swift.struct/remove(_:).md)
  Removes the given element and all elements subsumed by it.
- [func subtract(Self)](arview/debugoptions-swift.struct/subtract(_:).md)
  Removes the elements of the given set from this set.
- [func subtracting(Self) -> Self](arview/debugoptions-swift.struct/subtracting(_:).md)
  Returns a new set containing the elements of this set that do not occur in the given set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/debugoptions-swift.struct/insert(_:))*