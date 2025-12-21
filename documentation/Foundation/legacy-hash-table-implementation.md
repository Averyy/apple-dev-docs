# Legacy Hash Table Implementation

**Framework**: Foundation

## Topics

### Functions
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
- [func NSResetHashTable(NSHashTable<AnyObject>)](nsresethashtable(_:).md)
  Deletes the elements of the specified hash table.
- [func NSStringFromHashTable(NSHashTable<AnyObject>) -> String](nsstringfromhashtable(_:).md)
  Returns a string describing the hash table’s contents.
### Data Types
- [struct NSHashEnumerator](nshashenumerator.md)
  Allows successive elements of a hash table to be returned each time this structure is passed to [`NSNextHashEnumeratorItem(_:)`](nsnexthashenumeratoritem(_:).md).
- [struct NSHashTableCallBacks](nshashtablecallbacks.md)
  Defines a structure that contains the function pointers used to configure behavior of `NSHashTable` with respect to elements within a hash table.
- [typealias NSHashTableOptions](nshashtableoptions.md)
  Components in a bit-field to specify the behavior of elements in an [`NSHashTable`](nshashtable.md) object.
### Constants
- [let NSIntegerHashCallBacks: NSHashTableCallBacks](nsintegerhashcallbacks.md)
  For sets of `NSInteger`-sized quantities or smaller (for example, `int`, `long`, or `unichar`).
- [let NSNonOwnedPointerHashCallBacks: NSHashTableCallBacks](nsnonownedpointerhashcallbacks.md)
  For sets of pointers, hashed by address.
- [let NSNonRetainedObjectHashCallBacks: NSHashTableCallBacks](nsnonretainedobjecthashcallbacks.md)
  For sets of objects, but without retaining/releasing.
- [let NSObjectHashCallBacks: NSHashTableCallBacks](nsobjecthashcallbacks.md)
  For sets of objects (similar to `NSSet`).
- [let NSOwnedObjectIdentityHashCallBacks: NSHashTableCallBacks](nsownedobjectidentityhashcallbacks.md)
  For sets of objects, with transfer of ownership upon insertion, using pointer equality.
- [let NSOwnedPointerHashCallBacks: NSHashTableCallBacks](nsownedpointerhashcallbacks.md)
  For sets of pointers, with transfer of ownership upon insertion.
- [let NSPointerToStructHashCallBacks: NSHashTableCallBacks](nspointertostructhashcallbacks.md)
  For sets of pointers to structs, when the first field of the struct is `int`-sized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/legacy-hash-table-implementation)*