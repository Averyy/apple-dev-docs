# description

**Framework**: Group Activities  
**Kind**: property

A textual representation of this instance.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
final var description: String { get }
```

#### Discussion

Calling this property directly is discouraged. Instead, convert an instance of any type to a string by using the `String(describing:)` initializer. This initializer works with any type, and uses the custom `description` property for types that conform to `CustomStringConvertible`:

```swift
struct Point: CustomStringConvertible {
    let x: Int, y: Int

    var description: String {
        return "(\(x), \(y))"
    }
}

let p = Point(x: 21, y: 30)
let s = String(describing: p)
print(s)
// Prints "(21, 30)"
```

The conversion of `p` to a string in the assignment to `s` uses the `Point` type’s `description` property.

## See Also

- [var state: GroupSession<ActivityType>.State](groupsession/state-swift.property.md)
  The current state of the session.
- [GroupSession.State](groupsession/state-swift.enum.md)
  The possible states of a session.
- [let id: UUID](groupsession/id.md)
  The unique identifier of the current session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsession/description)*