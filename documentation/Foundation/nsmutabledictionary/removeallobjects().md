# removeAllObjects()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) removeAllObjects;
```

#### Discussion

Each key and corresponding value object is sent a [`release`](../../ObjectiveC/nsobject-c.protocol/release.md) message.

## See Also

### Removing Entries From a Mutable Dictionary
- [func removeObject(forKey: Any)](./removeobject%28forkey%29.md)
  Removes a given key and its associated value from the dictionary.
- [func removeObjects(forKeys: [Any])](./removeobjects%28forkeys%29.md)
  Removes from the dictionary entries specified by elements in a given array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutabledictionary/removeallobjects())*