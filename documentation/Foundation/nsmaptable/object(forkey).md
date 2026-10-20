# object(forKey:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (ObjectType) objectForKey:(KeyType) aKey;
```

#### Return Value

The value associated with `aKey`, or `nil` if no value is associated with `aKey`.

## Parameters

- `aKey`: The key for which to return the corresponding value.

## See Also

### Accessing Content
- [func keyEnumerator() -> NSEnumerator](./keyenumerator%28%29.md)
  Returns an enumerator object that lets you access each key in the map table.
- [func objectEnumerator() -> NSEnumerator?](./objectenumerator%28%29.md)
  Returns an enumerator object that lets you access each value in the map table.
- [var count: Int](./count.md)
  The number of key-value pairs in the map table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmaptable/object(forkey:))*