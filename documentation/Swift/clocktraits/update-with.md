# update(with:)

**Framework**: Swift  
**Kind**: method

Inserts the given element into the set.

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
mutating func update(with newMember: Self.Element) -> Self.Element?
```

#### Return Value

The intersection of `[newMember]` and the set if the intersection was nonempty; otherwise, `nil`.

#### Discussion

If `newMember` is not contained in the set but subsumes current members of the set, the subsumed members are returned.

```swift
var options: ShippingOptions = [.secondDay, .priority]
let replaced = options.update(with: .express)
print(replaced == .secondDay)
// Prints "true"
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/clocktraits/update(with:))*