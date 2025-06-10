# NSHashRemove(_:_:)

**Framework**: Foundation  
**Kind**: func

Removes an element from the specified hash table.

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
func NSHashRemove(_ table: NSHashTable<AnyObject>, _ pointer: UnsafeRawPointer?)
```

#### Discussion

If `pointer` matches an item already in `table`, this function releases the preexisting item.

## See Also

- [func NSHashInsertKnownAbsent(NSHashTable<AnyObject>, UnsafeRawPointer?)](nshashinsertknownabsent(_:_:).md)
  Adds an element to the specified hash table.
- [func NSHashInsert(NSHashTable<AnyObject>, UnsafeRawPointer?)](nshashinsert(_:_:).md)
  Adds an element to the specified hash table.
- [func NSHashInsertIfAbsent(NSHashTable<AnyObject>, UnsafeRawPointer?) -> UnsafeMutableRawPointer?](nshashinsertifabsent(_:_:).md)
  Adds an element to the specified hash table only if the table does not already contain the element.
- [func NSAllHashTableObjects(NSHashTable<AnyObject>) -> [Any]](nsallhashtableobjects(_:).md)
  Returns all of the elements in the specified hash table.
- [func NSCompareHashTables(NSHashTable<AnyObject>, NSHashTable<AnyObject>) -> Bool](nscomparehashtables(_:_:).md)
  Returns a Boolean value that indicates whether the elements of two hash tables are equal.
- [func NSCopyHashTableWithZone(NSHashTable<AnyObject>, NSZone?) -> NSHashTable<AnyObject>](nscopyhashtablewithzone(_:_:).md)
  Performs a shallow copy of the specified hash table.
- [func NSCountHashTable(NSHashTable<AnyObject>) -> Int](nscounthashtable(_:).md)
  Returns the number of elements in a hash table.
- [func NSCreateHashTable(NSHashTableCallBacks, Int) -> NSHashTable<AnyObject>](nscreatehashtable(_:_:).md)
  Creates and returns a new hash table.
- [func NSCreateHashTableWithZone(NSHashTableCallBacks, Int, NSZone?) -> NSHashTable<AnyObject>](nscreatehashtablewithzone(_:_:_:).md)
  Creates a new hash table in a given zone.
- [func NSEndHashTableEnumeration(UnsafeMutablePointer<NSHashEnumerator>)](nsendhashtableenumeration(_:).md)
  Used when finished with an enumerator.
- [func NSEnumerateHashTable(NSHashTable<AnyObject>) -> NSHashEnumerator](nsenumeratehashtable(_:).md)
  Creates an enumerator for the specified hash table.
- [func NSFreeHashTable(NSHashTable<AnyObject>)](nsfreehashtable(_:).md)
  Deletes the specified hash table.
- [func NSHashGet(NSHashTable<AnyObject>, UnsafeRawPointer?) -> UnsafeMutableRawPointer](nshashget(_:_:).md)
  Returns an element of the hash table.
- [func NSHashInsert(NSHashTable<AnyObject>, UnsafeRawPointer?)](nshashinsert(_:_:).md)
  Adds an element to the specified hash table.
- [func NSHashInsertIfAbsent(NSHashTable<AnyObject>, UnsafeRawPointer?) -> UnsafeMutableRawPointer?](nshashinsertifabsent(_:_:).md)
  Adds an element to the specified hash table only if the table does not already contain the element.
- [func NSHashInsertKnownAbsent(NSHashTable<AnyObject>, UnsafeRawPointer?)](nshashinsertknownabsent(_:_:).md)
  Adds an element to the specified hash table.
- [func NSNextHashEnumeratorItem(UnsafeMutablePointer<NSHashEnumerator>) -> UnsafeMutableRawPointer?](nsnexthashenumeratoritem(_:).md)
  Returns the next hash-table element in the enumeration.
- [func NSResetHashTable(NSHashTable<AnyObject>)](nsresethashtable(_:).md)
  Deletes the elements of the specified hash table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nshashremove(_:_:))*