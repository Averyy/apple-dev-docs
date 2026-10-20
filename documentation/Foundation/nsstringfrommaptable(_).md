# NSStringFromMapTable(_:)

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Returns a string describing the map table’s contents.

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
func NSStringFromMapTable(_ table: NSMapTable<AnyObject, AnyObject>) -> String
```

```c
extern NSString *NSStringFromMapTable(NSMapTable *table);
```

#### Return Value

A string describing the map table’s contents.

#### Discussion

The function iterates over the key-value pairs of `table` and for each one appends the string “a = b;\n”, where a and b are the key and value strings returned by the corresponding `describe` callback functions. If `NULL` was specified for the callback function, a and b are the key and value pointers, expressed as hexadecimal numbers.

## Parameters

- `table`: A reference to a map table structure.

## See Also

### Functions
- [func NSAllMapTableKeys(NSMapTable<AnyObject, AnyObject>) -> [Any]](./nsallmaptablekeys%28_%29.md)
  Returns all of the keys in the specified map table.
- [func NSAllMapTableValues(NSMapTable<AnyObject, AnyObject>) -> [Any]](./nsallmaptablevalues%28_%29.md)
  Returns all of the values in the specified table.
- [func NSCompareMapTables(NSMapTable<AnyObject, AnyObject>, NSMapTable<AnyObject, AnyObject>) -> Bool](./nscomparemaptables%28_,_%29.md)
  Compares the elements of two map tables for equality.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstringfrommaptable(_:))*