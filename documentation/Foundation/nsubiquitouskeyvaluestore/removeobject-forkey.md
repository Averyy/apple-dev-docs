# removeObject(forKey:)

**Framework**: Foundation  
**Kind**: method

Removes the value associated with the specified key from the key-value store.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func removeObject(forKey aKey: String)
```

#### Discussion

If the specified key is not found in the key-value store, this method does nothing. This method removes the key from the in-memory version of the store only. Call the synchronize method at appropriate times to update the information on disk.

## Parameters

- `aKey`: The key corresponding to the value you want to remove.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/removeobject(forkey:))*