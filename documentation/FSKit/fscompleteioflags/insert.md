# insert(_:)

**Framework**: FSKit  
**Kind**: method

Adds the given element to the option set if it is not already a member.

**Availability**:
- macOS 15.4+

## Declaration

```swift
@discardableResult
mutating func insert(_ newMember: Self.Element) -> (inserted: Bool, memberAfterInsert: Self.Element)
```

#### Return Value

`(true, newMember)` if `newMember` was not contained in `self`. Otherwise, returns `(false, oldMember)`, where `oldMember` is the member of the set equal to `newMember`.

#### Discussion

In the following example, the `.secondDay` shipping option is added to the `freeOptions` option set if `purchasePrice` is greater than 50.0. For the `ShippingOptions` declaration, see the `OptionSet` protocol discussion.

```swift
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fscompleteioflags/insert(_:))*