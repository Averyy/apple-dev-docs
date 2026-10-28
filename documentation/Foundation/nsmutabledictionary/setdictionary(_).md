# setDictionary(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sets the contents of the receiving dictionary to entries in a given dictionary.

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
func setDictionary(_ otherDictionary: [AnyHashable : Any])
```

```objc
- (void) setDictionary:(NSDictionary<id,id> *) otherDictionary;
```

## Discussion

All entries are removed from the receiving dictionary (with [`removeAllObjects()`](./removeallobjects%28%29.md)), then each entry from `otherDictionary` added into the receiving dictionary.

## Parameters

- `otherDictionary`: A dictionary containing the new entries.

## See Also

### Adding Entries to a Mutable Dictionary
- [func setObject(Any, forKey: any NSCopying)](./setobject%28_,forkey%29.md)
  Adds a given key-value pair to the dictionary.
- [func setValue(Any?, forKey: String)](./setvalue%28_,forkey%29.md)
  Adds a given key-value pair to the dictionary.
- [func addEntries(from: [AnyHashable : Any])](./addentries%28from%29.md)
  Adds to the receiving dictionary the entries from another dictionary.
- [- setObject:forKeyedSubscript:](./setobject_forkeyedsubscript_.md)
  Adds a given key-value pair to the dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutabledictionary/setdictionary(_:))*