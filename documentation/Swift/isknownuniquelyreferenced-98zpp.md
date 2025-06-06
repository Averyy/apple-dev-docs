# isKnownUniquelyReferenced(_:)

**Framework**: Swift  
**Kind**: func

Returns a Boolean value indicating whether the given object is known to have a single strong reference.

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
func isKnownUniquelyReferenced<T>(_ object: inout T?) -> Bool where T : AnyObject
```

#### Return Value

`true` if `object` is known to have a single strong reference; otherwise, `false`. If `object` is `nil`, the return value is `false`.

#### Discussion

The `isKnownUniquelyReferenced(_:)` function is useful for implementing the copy-on-write optimization for the deep storage of value types:

```swift
mutating func update(withValue value: T) {
    if !isKnownUniquelyReferenced(&myStorage) {
        myStorage = self.copiedStorage()
    }
    myStorage.update(withValue: value)
}
```

`isKnownUniquelyReferenced(_:)` checks only for strong references to the given object—if `object` has additional weak or unowned references, the result may still be `true`. Because weak and unowned references cannot be the only reference to an object, passing a weak or unowned reference as `object` always results in `false`.

If the instance passed as `object` is being accessed by multiple threads simultaneously, this function may still return `true`. Therefore, you must only call this function from mutating methods with appropriate thread synchronization. That will ensure that `isKnownUniquelyReferenced(_:)` only returns `true` when there is really one accessor, or when there is a race condition, which is already undefined behavior.

## Parameters

- `object`: An instance of a class. This function does   modify   ; the use of   is an implementation artifact.

## See Also

- [func isKnownUniquelyReferenced<T>(inout T) -> Bool](isknownuniquelyreferenced(_:)-5kvtu.md)
  Returns a Boolean value indicating whether the given object is known to have a single strong reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/isknownuniquelyreferenced(_:)-98zpp)*