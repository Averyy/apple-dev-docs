# description

**Framework**: Swift  
**Kind**: property

A textual representation of this instance.

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
var description: String { get }
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

- [var debugDescription: String](character/debugdescription.md)
  A textual representation of the character, suitable for debugging.
- [var customMirror: Mirror](character/custommirror.md)
  A mirror that reflects the `Character` instance.
- [var customPlaygroundQuickLook: _PlaygroundQuickLook](character/customplaygroundquicklook.md)
  A custom playground Quick Look for the `Character` instance.
- [func hash(into: inout Hasher)](character/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/character/description)*