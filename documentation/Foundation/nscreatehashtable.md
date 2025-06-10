# NSCreateHashTable(_:_:)

**Framework**: Foundation  
**Kind**: func

Creates and returns a new hash table.

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
func NSCreateHashTable(_ callBacks: NSHashTableCallBacks, _ capacity: Int) -> NSHashTable<AnyObject>
```

#### Return Value

A pointer to an NSHashTable created in the default zone.

#### Discussion

The table’s size is dependent on (but generally not equal to) `capacity`. If `capacity` is 0, a small hash table is created. The [`NSHashTableCallBacks`](nshashtablecallbacks.md) structure `callBacks` has five pointers to functions, with the following defaults: pointer hashing, if `hash` is `NULL`; pointer equality, if `isEqual` is `NULL`; no callback upon adding an element, if `retain` is `NULL`; no callback upon removing an element, if `release` is `NULL`; and a function returning a pointer’s hexadecimal value as a string, if `describe` is `NULL`. The hashing function must be defined such that if two data elements are equal, as defined by the comparison function, the values produced by hashing on these elements must also be equal. Also, data elements must remain invariant if the value of the hashing function depends on them; for example, if the hashing function operates directly on the characters of a string, that string can’t change.

## See Also

- [func NSCreateHashTableWithZone(NSHashTableCallBacks, Int, NSZone?) -> NSHashTable<AnyObject>](nscreatehashtablewithzone(_:_:_:).md)
  Creates a new hash table in a given zone.
- [func NSCopyHashTableWithZone(NSHashTable<AnyObject>, NSZone?) -> NSHashTable<AnyObject>](nscopyhashtablewithzone(_:_:).md)
  Performs a shallow copy of the specified hash table.
- [func NSAllHashTableObjects(NSHashTable<AnyObject>) -> [Any]](nsallhashtableobjects(_:).md)
  Returns all of the elements in the specified hash table.
- [func NSCompareHashTables(NSHashTable<AnyObject>, NSHashTable<AnyObject>) -> Bool](nscomparehashtables(_:_:).md)
  Returns a Boolean value that indicates whether the elements of two hash tables are equal.
- [func NSCopyHashTableWithZone(NSHashTable<AnyObject>, NSZone?) -> NSHashTable<AnyObject>](nscopyhashtablewithzone(_:_:).md)
  Performs a shallow copy of the specified hash table.
- [func NSCountHashTable(NSHashTable<AnyObject>) -> Int](nscounthashtable(_:).md)
  Returns the number of elements in a hash table.
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
- [func NSHashRemove(NSHashTable<AnyObject>, UnsafeRawPointer?)](nshashremove(_:_:).md)
  Removes an element from the specified hash table.
- [func NSNextHashEnumeratorItem(UnsafeMutablePointer<NSHashEnumerator>) -> UnsafeMutableRawPointer?](nsnexthashenumeratoritem(_:).md)
  Returns the next hash-table element in the enumeration.
- [func NSResetHashTable(NSHashTable<AnyObject>)](nsresethashtable(_:).md)
  Deletes the elements of the specified hash table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscreatehashtable(_:_:))*