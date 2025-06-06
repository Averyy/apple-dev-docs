# Legacy Map Table Implementation

**Framework**: Foundation

## Topics

### Functions
- [func NSAllMapTableKeys(NSMapTable<AnyObject, AnyObject>) -> [Any]](nsallmaptablekeys(_:).md)
  Returns all of the keys in the specified map table.
- [func NSAllMapTableValues(NSMapTable<AnyObject, AnyObject>) -> [Any]](nsallmaptablevalues(_:).md)
  Returns all of the values in the specified table.
- [func NSCompareMapTables(NSMapTable<AnyObject, AnyObject>, NSMapTable<AnyObject, AnyObject>) -> Bool](nscomparemaptables(_:_:).md)
  Compares the elements of two map tables for equality.
- [func NSCopyMapTableWithZone(NSMapTable<AnyObject, AnyObject>, NSZone?) -> NSMapTable<AnyObject, AnyObject>](nscopymaptablewithzone(_:_:).md)
  Performs a shallow copy of the specified map table.
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
- [func NSNextMapEnumeratorPair(UnsafeMutablePointer<NSMapEnumerator>, UnsafeMutablePointer<UnsafeMutableRawPointer?>?, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> Bool](nsnextmapenumeratorpair(_:_:_:).md)
  Returns a Boolean value that indicates whether the next map-table pair in the enumeration are set.
- [func NSResetMapTable(NSMapTable<AnyObject, AnyObject>)](nsresetmaptable(_:).md)
  Deletes the elements of the specified map table.
- [func NSStringFromMapTable(NSMapTable<AnyObject, AnyObject>) -> String](nsstringfrommaptable(_:).md)
  Returns a string describing the map table’s contents.
### Data Types
- [struct NSMapEnumerator](nsmapenumerator.md)
  Allows successive elements of a map table to be returned each time this structure is passed to [`NSNextMapEnumeratorPair(_:_:_:)`](nsnextmapenumeratorpair(_:_:_:).md).
- [NSMapTable](legacy-nsmaptable.md)
  The opaque data type used by the functions described in Managing Map Tables.
- [struct NSMapTableKeyCallBacks](nsmaptablekeycallbacks.md)
  The function pointers used to configure behavior of `NSMapTable` with respect to key elements within a map table.
- [typealias NSMapTableOptions](nsmaptableoptions.md)
  Constants used as components in a bitfield to specify the behavior of elements (keys and values) in an `NSMapTable` object.
- [struct NSMapTableValueCallBacks](nsmaptablevaluecallbacks.md)
  The function pointers used to configure behavior of `NSMapTable` with respect to value elements within a map table.
### Constants
- [let NSIntegerMapKeyCallBacks: NSMapTableKeyCallBacks](nsintegermapkeycallbacks.md)
  For keys that are pointer-sized quantities or smaller (for example, `int`, `long`, or `unichar`).
- [let NSIntMapKeyCallBacks: NSMapTableKeyCallBacks](nsintmapkeycallbacks.md)
  For keys that are pointer-sized quantities or smaller (for example, `int`, `long`, or `unichar`).
- [let NSNonOwnedPointerMapKeyCallBacks: NSMapTableKeyCallBacks](nsnonownedpointermapkeycallbacks.md)
  For keys that are pointers not freed.
- [let NSNonOwnedPointerOrNullMapKeyCallBacks: NSMapTableKeyCallBacks](nsnonownedpointerornullmapkeycallbacks.md)
  For keys that are pointers not freed, or `NULL`.
- [let NSNonRetainedObjectMapKeyCallBacks: NSMapTableKeyCallBacks](nsnonretainedobjectmapkeycallbacks.md)
  For sets of objects, but without retaining/releasing.
- [let NSObjectMapKeyCallBacks: NSMapTableKeyCallBacks](nsobjectmapkeycallbacks.md)
  For keys that are objects.
- [let NSOwnedPointerMapKeyCallBacks: NSMapTableKeyCallBacks](nsownedpointermapkeycallbacks.md)
  For keys that are pointers, with transfer of ownership upon insertion.
### Constants
- [let NSIntegerMapValueCallBacks: NSMapTableValueCallBacks](nsintegermapvaluecallbacks.md)
  For values that are pointer-sized quantities, (for example, `int`, `long`, or `unichar`).
- [let NSIntMapValueCallBacks: NSMapTableValueCallBacks](nsintmapvaluecallbacks.md)
  For values that are pointer-sized quantities, (for example, `int`, `long`, or `unichar`).
- [let NSNonOwnedPointerMapValueCallBacks: NSMapTableValueCallBacks](nsnonownedpointermapvaluecallbacks.md)
  For values that are not owned pointers.
- [let NSOwnedPointerMapValueCallBacks: NSMapTableValueCallBacks](nsownedpointermapvaluecallbacks.md)
  For values that are owned pointers.
- [let NSNonRetainedObjectMapValueCallBacks: NSMapTableValueCallBacks](nsnonretainedobjectmapvaluecallbacks.md)
  For sets of objects, but without retaining/releasing.
- [let NSObjectMapValueCallBacks: NSMapTableValueCallBacks](nsobjectmapvaluecallbacks.md)
  For values that are objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/legacy-map-table-implementation)*