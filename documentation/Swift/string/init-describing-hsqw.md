# init(describing:)

**Framework**: Swift  
**Kind**: init

Creates a string representing the given value.

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
init<Subject>(describing instance: Subject) where Subject : CustomStringConvertible
```

#### Discussion

Use this initializer to convert an instance of any type to its preferred representation as a `String` instance. The initializer creates the string representation of `instance` in one of the following ways, depending on its protocol conformance:

- If `instance` conforms to the `TextOutputStreamable` protocol, the result is obtained by calling `instance.write(to: s)` on an empty string `s`.
- If `instance` conforms to the `CustomStringConvertible` protocol, the result is `instance.description`.
- If `instance` conforms to the `CustomDebugStringConvertible` protocol, the result is `instance.debugDescription`.
- An unspecified result is supplied automatically by the Swift standard library.

For example, this custom `Point` struct uses the default representation supplied by the standard library.

```swift
struct Point {
    let x: Int, y: Int
}

let p = Point(x: 21, y: 30)
print(String(describing: p))
// Prints "Point(x: 21, y: 30)"
```

After adding `CustomStringConvertible` conformance by implementing the `description` property, `Point` provides its own custom representation.

```swift
extension Point: CustomStringConvertible {
    var description: String {
        return "(\(x), \(y))"
    }
}

print(String(describing: p))
// Prints "(21, 30)"
```

## See Also

- [init<T>(T)](string/init(_:)-1ywfq.md)
  Creates an instance from the description of a given `LosslessStringConvertible` instance.
- [init<Subject>(describing: Subject)](string/init(describing:)-588wb.md)
  Creates a string representing the given value.
- [init<Subject>(describing: Subject)](string/init(describing:)-6ttci.md)
  Creates a string representing the given value.
- [init<Subject>(describing: Subject)](string/init(describing:)-67ncf.md)
  Creates a string representing the given value.
- [init<Subject>(reflecting: Subject)](string/init(reflecting:).md)
  Creates a string with a detailed representation of the given value, suitable for debugging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/init(describing:)-hsqw)*