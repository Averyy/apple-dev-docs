# update(with:)

**Framework**: Create ML  
**Kind**: method

Inserts the given element into the set.

**Availability**:
- macOS 10.14+

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

- [func insert(Self.Element) -> (inserted: Bool, memberAfterInsert: Self.Element)](mlactionclassifier/videoaugmentationoptions/insert(_:).md)
  Adds the given element to the option set if it is not already a member.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/videoaugmentationoptions/update(with:))*