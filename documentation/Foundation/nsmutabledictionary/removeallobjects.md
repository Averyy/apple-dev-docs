# removeAllObjects()

**Framework**: Foundation  
**Kind**: method

Empties the dictionary of its entries.

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
func removeAllObjects()
```

#### Discussion

Each key and corresponding value object is sent a [`release`](https://developer.apple.com/documentation/objectivec/1418956-nsobject/1571957-release) message.

## See Also

- [func removeObject(forKey: Any)](nsmutabledictionary/removeobject(forkey:).md)
  Removes a given key and its associated value from the dictionary.
- [func removeObjects(forKeys: [Any])](nsmutabledictionary/removeobjects(forkeys:).md)
  Removes from the dictionary entries specified by elements in a given array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutabledictionary/removeallobjects())*