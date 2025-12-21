# NSMapMember(_:_:_:_:)

**Framework**: Foundation  
**Kind**: func

Indicates whether a given table contains a given key.

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
func NSMapMember(_ table: NSMapTable<AnyObject, AnyObject>, _ key: UnsafeRawPointer, _ originalKey: UnsafeMutablePointer<UnsafeMutableRawPointer?>?, _ value: UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if `table` contains a key equal to `key`, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

If `table` contains a key equal to `key`, `originalKey` is set to `key`, and `value` is set to the value that `table` maps to `key`.

## See Also

- [func NSNextMapEnumeratorPair(UnsafeMutablePointer<NSMapEnumerator>, UnsafeMutablePointer<UnsafeMutableRawPointer?>?, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> Bool](nsnextmapenumeratorpair(_:_:_:).md)
  Returns a Boolean value that indicates whether the next map-table pair in the enumeration are set.
- [func NSAllMapTableValues(NSMapTable<AnyObject, AnyObject>) -> [Any]](nsallmaptablevalues(_:).md)
  Returns all of the values in the specified table.
- [func NSMapGet(NSMapTable<AnyObject, AnyObject>, UnsafeRawPointer?) -> UnsafeMutableRawPointer?](nsmapget(_:_:).md)
  Returns a map table value for the specified key.
- [func NSEnumerateMapTable(NSMapTable<AnyObject, AnyObject>) -> NSMapEnumerator](nsenumeratemaptable(_:).md)
  Creates an enumerator for the specified map table.
- [func NSAllMapTableKeys(NSMapTable<AnyObject, AnyObject>) -> [Any]](nsallmaptablekeys(_:).md)
  Returns all of the keys in the specified map table.
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
- [func NSMapRemove(NSMapTable<AnyObject, AnyObject>, UnsafeRawPointer?)](nsmapremove(_:_:).md)
  Removes a key and corresponding value from the specified table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmapmember(_:_:_:_:))*