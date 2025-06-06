# removeObjects(forKeys:)

**Framework**: Foundation  
**Kind**: method

Removes from the dictionary entries specified by elements in a given array.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func removeObjects(forKeys keyArray: [Any])
```

#### Discussion

If a key in `keyArray` does not exist, the entry is ignored.

## Parameters

- `keyArray`: An array of objects specifying the keys to remove.

## See Also

- [func removeObject(forKey: Any)](nsmutabledictionary/removeobject(forkey:).md)
  Removes a given key and its associated value from the dictionary.
- [func removeAllObjects()](nsmutabledictionary/removeallobjects.md)
  Empties the dictionary of its entries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutabledictionary/removeobjects(forkeys:))*