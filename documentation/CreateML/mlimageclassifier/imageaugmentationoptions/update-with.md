# update(with:)

**Framework**: Create ML  
**Kind**: method

Inserts the given element into the set.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
@discardableResult
mutating func update(with newMember: Self.Element) -> Self.Element?
```

#### Return Value

The intersection of `[newMember]` and the set if the intersection was nonempty; otherwise, `nil`.

#### Discussion

If `newMember` is not contained in the set but subsumes current members of the set, the subsumed members are returned.

```None
var options: ShippingOptions = [.secondDay, .priority]
let replaced = options.update(with: .express)
print(replaced == .secondDay)
// Prints "true"
```

## See Also

- [func insert(Self.Element) -> (inserted: Bool, memberAfterInsert: Self.Element)](mlimageclassifier/imageaugmentationoptions/insert(_:).md)
  Adds the given element to the option set if it is not already a member.
- [func remove(Self.Element) -> Self.Element?](mlimageclassifier/imageaugmentationoptions/remove(_:).md)
  Removes the given element and all elements subsumed by it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/imageaugmentationoptions/update(with:))*