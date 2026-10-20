# hashValue

**Framework**: Swift  
**Kind**: property  
**Role**: Instance Property

The hash value.

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
var hashValue: Int { get }
```

Available when `Element` conforms to `Hashable`.

#### Discussion

Hash values are not guaranteed to be equal across different executions of your program. Do not save hash values to use during a future execution.

> ❗ **Important**: `hashValue` is deprecated as a `Hashable` requirement. To conform to `Hashable`, implement the `hash(into:)` requirement instead. The compiler provides an implementation for `hashValue` for you.

## See Also

### Infrequently Used Functionality
- [init(arrayLiteral: Element...)](./init%28arrayliteral%29.md)
  Creates an array from the given array literal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/hashvalue)*