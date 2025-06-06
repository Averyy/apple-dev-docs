# hashValue

**Framework**: DeviceActivity  
**Kind**: property

The hash value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var hashValue: Int { get }
```

#### Discussion

Hash values aren’t guaranteed to be equal across different executions of your program. Don’t save hash values to use during a future execution.

> ❗ **Important**: `hashValue` is deprecated as a Hashable requirement. To conform to [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable), implement the [`hash(into:)`](deviceactivityevent/name/hash(into:).md) requirement instead.

`hashValue` is deprecated as a Hashable requirement. To conform to [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable), implement the [`hash(into:)`](deviceactivityevent/name/hash(into:).md) requirement instead.

## See Also

- [func hash(into: inout Hasher)](deviceactivityevent/name/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [static func != (Self, Self) -> Bool](deviceactivityevent/name/!=(_:_:).md)
  Returns a Boolean value that indicates whether two values aren’t equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityevent/name/hashvalue)*