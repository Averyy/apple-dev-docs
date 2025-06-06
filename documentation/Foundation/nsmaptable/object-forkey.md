# object(forKey:)

**Framework**: Foundation  
**Kind**: method

Returns a the value associated with a given key.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func object(forKey aKey: KeyType?) -> ObjectType?
```

#### Return Value

The value associated with `aKey`, or `nil` if no value is associated with `aKey`.

## Parameters

- `aKey`: The key for which to return the corresponding value.

## See Also

- [func keyEnumerator() -> NSEnumerator](nsmaptable/keyenumerator.md)
  Returns an enumerator object that lets you access each key in the map table.
- [func objectEnumerator() -> NSEnumerator?](nsmaptable/objectenumerator.md)
  Returns an enumerator object that lets you access each value in the map table.
- [var count: Int](nsmaptable/count.md)
  The number of key-value pairs in the map table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmaptable/object(forkey:))*