# removeObject(forKey:)

**Framework**: Foundation  
**Kind**: method

Removes a given key and its associated value from the map table.

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
func removeObject(forKey aKey: KeyType?)
```

#### Discussion

Does nothing if `aKey` does not exist.

## Parameters

- `aKey`: The key to remove.

## See Also

- [func setObject(ObjectType?, forKey: KeyType?)](nsmaptable/setobject(_:forkey:).md)
  Adds a given key-value pair to the map table.
- [func removeAllObjects()](nsmaptable/removeallobjects.md)
  Empties the map table of its entries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmaptable/removeobject(forkey:))*