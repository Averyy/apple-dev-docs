# update(with:)

**Framework**: UIKit  
**Kind**: method

Inserts the given element into the set.

**Availability**:
- iOS ?+
- iPadOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaxis/update(with:))*