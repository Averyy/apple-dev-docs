# removeObject(forKey:)

**Framework**: Foundation  
**Kind**: method

Removes a given key and its associated value from the dictionary.

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
func removeObject(forKey aKey: Any)
```

#### Discussion

Does nothing if `aKey` does not exist.

For example, assume you have an archived dictionary that records the call letters and associated frequencies of radio stations. To remove an entry for a defunct station, you could write code similar to the following:

```objc
NSMutableDictionary *stations = nil;
 
stations = [[NSMutableDictionary alloc]
        initWithContentsOfFile: pathToArchive];
[stations removeObjectForKey:@"KIKT"];
```

## Parameters

- `aKey`: The key to remove.

## See Also

- [func removeAllObjects()](nsmutabledictionary/removeallobjects.md)
  Empties the dictionary of its entries.
- [func removeObjects(forKeys: [Any])](nsmutabledictionary/removeobjects(forkeys:).md)
  Removes from the dictionary entries specified by elements in a given array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutabledictionary/removeobject(forkey:))*