# NSEnumerateHashTable(_:)

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Creates an enumerator for the specified hash table.

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
func NSEnumerateHashTable(_ table: NSHashTable<AnyObject>) -> NSHashEnumerator
```

```c
extern NSHashEnumerator NSEnumerateHashTable(NSHashTable *table);
```

#### Return Value

An NSHashEnumerator structure that will cause successive elements of `table` to be returned each time this enumerator is passed to `NSNextHashEnumeratorItem`.

## See Also

### Related Documentation
- [func NSNextHashEnumeratorItem(UnsafeMutablePointer<NSHashEnumerator>) -> UnsafeMutableRawPointer?](./nsnexthashenumeratoritem%28_%29.md)
  Returns the next hash-table element in the enumeration.
### Functions
- [func NSAllHashTableObjects(NSHashTable<AnyObject>) -> [Any]](./nsallhashtableobjects%28_%29.md)
  Returns all of the elements in the specified hash table.
- [func NSCompareHashTables(NSHashTable<AnyObject>, NSHashTable<AnyObject>) -> Bool](./nscomparehashtables%28_,_%29.md)
  Returns a Boolean value that indicates whether the elements of two hash tables are equal.
- [func NSCopyHashTableWithZone(NSHashTable<AnyObject>, NSZone?) -> NSHashTable<AnyObject>](./nscopyhashtablewithzone%28_,_%29.md)
  Performs a shallow copy of the specified hash table.
- [func NSCountHashTable(NSHashTable<AnyObject>) -> Int](./nscounthashtable%28_%29.md)
  Returns the number of elements in a hash table.
- [func NSCreateHashTable(NSHashTableCallBacks, Int) -> NSHashTable<AnyObject>](./nscreatehashtable%28_,_%29.md)
  Creates and returns a new hash table.
- [func NSCreateHashTableWithZone(NSHashTableCallBacks, Int, NSZone?) -> NSHashTable<AnyObject>](./nscreatehashtablewithzone%28_,_,_%29.md)
  Creates a new hash table in a given zone.
- [func NSEndHashTableEnumeration(UnsafeMutablePointer<NSHashEnumerator>)](./nsendhashtableenumeration%28_%29.md)
  Used when finished with an enumerator.
- [func NSFreeHashTable(NSHashTable<AnyObject>)](./nsfreehashtable%28_%29.md)
  Deletes the specified hash table.
- [func NSHashGet(NSHashTable<AnyObject>, UnsafeRawPointer?) -> UnsafeMutableRawPointer](./nshashget%28_,_%29.md)
  Returns an element of the hash table.
- [func NSHashInsert(NSHashTable<AnyObject>, UnsafeRawPointer?)](./nshashinsert%28_,_%29.md)
  Adds an element to the specified hash table.
- [func NSHashInsertIfAbsent(NSHashTable<AnyObject>, UnsafeRawPointer?) -> UnsafeMutableRawPointer?](./nshashinsertifabsent%28_,_%29.md)
  Adds an element to the specified hash table only if the table does not already contain the element.
- [func NSHashInsertKnownAbsent(NSHashTable<AnyObject>, UnsafeRawPointer?)](./nshashinsertknownabsent%28_,_%29.md)
  Adds an element to the specified hash table.
- [func NSHashRemove(NSHashTable<AnyObject>, UnsafeRawPointer?)](./nshashremove%28_,_%29.md)
  Removes an element from the specified hash table.
- [func NSNextHashEnumeratorItem(UnsafeMutablePointer<NSHashEnumerator>) -> UnsafeMutableRawPointer?](./nsnexthashenumeratoritem%28_%29.md)
  Returns the next hash-table element in the enumeration.
- [func NSResetHashTable(NSHashTable<AnyObject>)](./nsresethashtable%28_%29.md)
  Deletes the elements of the specified hash table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsenumeratehashtable(_:))*