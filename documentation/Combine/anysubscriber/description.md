# description

**Framework**: Combine  
**Kind**: property

A textual representation of this instance.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

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

- [let combineIdentifier: CombineIdentifier](anysubscriber/combineidentifier.md)
  A unique identifier for identifying publisher streams.
- [var customMirror: Mirror](anysubscriber/custommirror.md)
  The custom mirror for this instance.
- [var playgroundDescription: Any](anysubscriber/playgrounddescription.md)
  A custom playground description for this instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/anysubscriber/description)*