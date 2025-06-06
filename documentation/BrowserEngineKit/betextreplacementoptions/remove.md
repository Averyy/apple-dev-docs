# remove(_:)

**Framework**: BrowserEngineKit  
**Kind**: method

Removes the given element and all elements subsumed by it.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS ?+
- visionOS ?+

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextreplacementoptions/remove(_:))*