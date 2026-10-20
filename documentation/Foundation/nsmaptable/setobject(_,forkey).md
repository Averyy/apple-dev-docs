# setObject(_:forKey:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Adds a given key-value pair to the map table.

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
func setObject(_ anObject: ObjectType?, forKey aKey: KeyType?)
```

```objc
- (void) setObject:(ObjectType) anObject forKey:(KeyType) aKey;
```

## Parameters

- `anObject`: The value for `aKey`.
- `aKey`: The key for `anObject`.

## See Also

### Manipulating Content
- [func removeObject(forKey: KeyType?)](./removeobject%28forkey%29.md)
  Removes a given key and its associated value from the map table.
- [func removeAllObjects()](./removeallobjects%28%29.md)
  Empties the map table of its entries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmaptable/setobject(_:forkey:))*