# NSCopyMapTableWithZone(_:_:)

**Framework**: Foundation  
**Kind**: func

Performs a shallow copy of the specified map table.

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
func NSCopyMapTableWithZone(_ table: NSMapTable<AnyObject, AnyObject>, _ zone: NSZone?) -> NSMapTable<AnyObject, AnyObject>
```

#### Return Value

A pointer to a new copy of `table`, created in `zone` and containing pointers to the keys and values of `table`.

#### Discussion

If `zone` is `NULL`, the new table is created in the default zone.

The new table adopts the callback functions of `table` and calls the `hash` and `retain` callback functions as appropriate when inserting elements into the new table.

## See Also

- [func NSCreateMapTableWithZone(NSMapTableKeyCallBacks, NSMapTableValueCallBacks, Int, NSZone?) -> NSMapTable<AnyObject, AnyObject>](nscreatemaptablewithzone(_:_:_:_:).md)
  Creates a new map table in the specified zone.
- [func NSCreateMapTable(NSMapTableKeyCallBacks, NSMapTableValueCallBacks, Int) -> NSMapTable<AnyObject, AnyObject>](nscreatemaptable(_:_:_:).md)
  Creates a new map table in the default zone.
- [struct NSMapTableValueCallBacks](nsmaptablevaluecallbacks.md)
  The function pointers used to configure behavior of `NSMapTable` with respect to value elements within a map table.
- [struct NSMapTableKeyCallBacks](nsmaptablekeycallbacks.md)
  The function pointers used to configure behavior of `NSMapTable` with respect to key elements within a map table.
- [func NSAllMapTableKeys(NSMapTable<AnyObject, AnyObject>) -> [Any]](nsallmaptablekeys(_:).md)
  Returns all of the keys in the specified map table.
- [func NSAllMapTableValues(NSMapTable<AnyObject, AnyObject>) -> [Any]](nsallmaptablevalues(_:).md)
  Returns all of the values in the specified table.
- [func NSCompareMapTables(NSMapTable<AnyObject, AnyObject>, NSMapTable<AnyObject, AnyObject>) -> Bool](nscomparemaptables(_:_:).md)
  Compares the elements of two map tables for equality.
- [func NSCountMapTable(NSMapTable<AnyObject, AnyObject>) -> Int](nscountmaptable(_:).md)
  Returns the number of elements in a map table.
- [func NSCreateMapTable(NSMapTableKeyCallBacks, NSMapTableValueCallBacks, Int) -> NSMapTable<AnyObject, AnyObject>](nscreatemaptable(_:_:_:).md)
  Creates a new map table in the default zone.
- [func NSCreateMapTableWithZone(NSMapTableKeyCallBacks, NSMapTableValueCallBacks, Int, NSZone?) -> NSMapTable<AnyObject, AnyObject>](nscreatemaptablewithzone(_:_:_:_:).md)
  Creates a new map table in the specified zone.
- [func NSEndMapTableEnumeration(UnsafeMutablePointer<NSMapEnumerator>)](nsendmaptableenumeration(_:).md)
  Used when finished with an enumerator.
- [func NSEnumerateMapTable(NSMapTable<AnyObject, AnyObject>) -> NSMapEnumerator](nsenumeratemaptable(_:).md)
  Creates an enumerator for the specified map table.
- [func NSFreeMapTable(NSMapTable<AnyObject, AnyObject>)](nsfreemaptable(_:).md)
  Deletes the specified map table.
- [func NSMapGet(NSMapTable<AnyObject, AnyObject>, UnsafeRawPointer?) -> UnsafeMutableRawPointer?](nsmapget(_:_:).md)
  Returns a map table value for the specified key.
- [func NSMapInsert(NSMapTable<AnyObject, AnyObject>, UnsafeRawPointer?, UnsafeRawPointer?)](nsmapinsert(_:_:_:).md)
  Inserts a key-value pair into the specified table.
- [func NSMapInsertIfAbsent(NSMapTable<AnyObject, AnyObject>, UnsafeRawPointer?, UnsafeRawPointer?) -> UnsafeMutableRawPointer?](nsmapinsertifabsent(_:_:_:).md)
  Inserts a key-value pair into the specified table.
- [func NSMapInsertKnownAbsent(NSMapTable<AnyObject, AnyObject>, UnsafeRawPointer?, UnsafeRawPointer?)](nsmapinsertknownabsent(_:_:_:).md)
  Inserts a key-value pair into the specified table if the pair had not been previously added.
- [func NSMapMember(NSMapTable<AnyObject, AnyObject>, UnsafeRawPointer, UnsafeMutablePointer<UnsafeMutableRawPointer?>?, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> Bool](nsmapmember(_:_:_:_:).md)
  Indicates whether a given table contains a given key.
- [func NSMapRemove(NSMapTable<AnyObject, AnyObject>, UnsafeRawPointer?)](nsmapremove(_:_:).md)
  Removes a key and corresponding value from the specified table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscopymaptablewithzone(_:_:))*