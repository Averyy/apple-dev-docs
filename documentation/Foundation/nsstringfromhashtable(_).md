# NSStringFromHashTable(_:)

**Framework**: Foundation  
**Kind**: func

Returns a string describing the hash table’s contents.

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
func NSStringFromHashTable(_ table: NSHashTable<AnyObject>) -> String
```

#### Return Value

A string describing `table`’s contents.

#### Discussion

The function iterates over the elements of `table`, and for each one appends the string returned by the `describe` callback function. If `NULL` was specified for the callback function, the hexadecimal value of each pointer is added to the string.

## See Also

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
- [func NSHashRemove(NSHashTable<AnyObject>, UnsafeRawPointer?)](nshashremove(_:_:).md)
  Removes an element from the specified hash table.
- [func NSNextHashEnumeratorItem(UnsafeMutablePointer<NSHashEnumerator>) -> UnsafeMutableRawPointer?](nsnexthashenumeratoritem(_:).md)
  Returns the next hash-table element in the enumeration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstringfromhashtable(_:))*