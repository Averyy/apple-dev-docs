# debugDescription

**Framework**: App Intents  
**Kind**: property

A textual representation of this instance, suitable for debugging.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
var debugDescription: String { get }
```

#### Discussion

Calling this property directly is discouraged. Instead, convert an instance of any type to a string by using the `String(reflecting:)` initializer. This initializer works with any type, and uses the custom `debugDescription` property for types that conform to `CustomDebugStringConvertible`:

```swift
struct Point: CustomDebugStringConvertible {
    let x: Int, y: Int

    var debugDescription: String {
        return "(\(x), \(y))"
    }
}

let p = Point(x: 21, y: 30)
let s = String(reflecting: p)
print(s)
// Prints "(21, 30)"
```

The conversion of `p` to a string in the assignment to `s` uses the `Point` type’s `debugDescription` property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentmodes/current/debugdescription)*