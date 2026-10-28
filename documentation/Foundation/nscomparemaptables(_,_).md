# NSCompareMapTables(_:_:)

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Compares the elements of two map tables for equality.

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
func NSCompareMapTables(_ table1: NSMapTable<AnyObject, AnyObject>, _ table2: NSMapTable<AnyObject, AnyObject>) -> Bool
```

```c
extern BOOL NSCompareMapTables(NSMapTable *table1, NSMapTable *table2);
```

## Return Value

[`true`](../Swift/true.md) if the keys and corresponding values of `table1` and `table2` are the same, and the two tables are the same size, otherwise [`false`](../Swift/false.md).

## See Also

### Related Documentation
- [func NSCreateMapTableWithZone(NSMapTableKeyCallBacks, NSMapTableValueCallBacks, Int, NSZone?) -> NSMapTable<AnyObject, AnyObject>](./nscreatemaptablewithzone%28_,_,_,_%29.md)
  Creates a new map table in the specified zone.
- [func NSCreateMapTable(NSMapTableKeyCallBacks, NSMapTableValueCallBacks, Int) -> NSMapTable<AnyObject, AnyObject>](./nscreatemaptable%28_,_,_%29.md)
  Creates a new map table in the default zone.
### Functions
- [func NSAllMapTableKeys(NSMapTable<AnyObject, AnyObject>) -> [Any]](./nsallmaptablekeys%28_%29.md)
  Returns all of the keys in the specified map table.
- [func NSAllMapTableValues(NSMapTable<AnyObject, AnyObject>) -> [Any]](./nsallmaptablevalues%28_%29.md)
  Returns all of the values in the specified table.
- [func NSCopyMapTableWithZone(NSMapTable<AnyObject, AnyObject>, NSZone?) -> NSMapTable<AnyObject, AnyObject>](./nscopymaptablewithzone%28_,_%29.md)
  Performs a shallow copy of the specified map table.
- [func NSCountMapTable(NSMapTable<AnyObject, AnyObject>) -> Int](./nscountmaptable%28_%29.md)
  Returns the number of elements in a map table.
- [func NSCreateMapTable(NSMapTableKeyCallBacks, NSMapTableValueCallBacks, Int) -> NSMapTable<AnyObject, AnyObject>](./nscreatemaptable%28_,_,_%29.md)
  Creates a new map table in the default zone.
- [func NSCreateMapTableWithZone(NSMapTableKeyCallBacks, NSMapTableValueCallBacks, Int, NSZone?) -> NSMapTable<AnyObject, AnyObject>](./nscreatemaptablewithzone%28_,_,_,_%29.md)
  Creates a new map table in the specified zone.
- [func NSEndMapTableEnumeration(UnsafeMutablePointer<NSMapEnumerator>)](./nsendmaptableenumeration%28_%29.md)
  Used when finished with an enumerator.
- [func NSEnumerateMapTable(NSMapTable<AnyObject, AnyObject>) -> NSMapEnumerator](./nsenumeratemaptable%28_%29.md)
  Creates an enumerator for the specified map table.
- [func NSFreeMapTable(consuming NSMapTable<AnyObject, AnyObject>)](./nsfreemaptable%28_%29.md)
  Deletes the specified map table.
- [func NSMapGet(NSMapTable<AnyObject, AnyObject>, UnsafeRawPointer?) -> UnsafeMutableRawPointer?](./nsmapget%28_,_%29.md)
  Returns a map table value for the specified key.
- [func NSMapInsert(NSMapTable<AnyObject, AnyObject>, UnsafeRawPointer?, UnsafeRawPointer?)](./nsmapinsert%28_,_,_%29.md)
  Inserts a key-value pair into the specified table.
- [func NSMapInsertIfAbsent(NSMapTable<AnyObject, AnyObject>, UnsafeRawPointer?, UnsafeRawPointer?) -> UnsafeMutableRawPointer?](./nsmapinsertifabsent%28_,_,_%29.md)
  Inserts a key-value pair into the specified table.
- [func NSMapInsertKnownAbsent(NSMapTable<AnyObject, AnyObject>, UnsafeRawPointer?, UnsafeRawPointer?)](./nsmapinsertknownabsent%28_,_,_%29.md)
  Inserts a key-value pair into the specified table if the pair had not been previously added.
- [func NSMapMember(NSMapTable<AnyObject, AnyObject>, UnsafeRawPointer, UnsafeMutablePointer<UnsafeMutableRawPointer?>?, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> Bool](./nsmapmember%28_,_,_,_%29.md)
  Indicates whether a given table contains a given key.
- [func NSMapRemove(NSMapTable<AnyObject, AnyObject>, UnsafeRawPointer?)](./nsmapremove%28_,_%29.md)
  Removes a key and corresponding value from the specified table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscomparemaptables(_:_:))*