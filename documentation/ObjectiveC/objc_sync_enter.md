# objc_sync_enter

**Framework**: Objective-C Runtime  
**Kind**: func  
**Role**: Function

Begin synchronizing on ‘obj’.
Allocates recursive pthread_mutex associated with ‘obj’ if needed.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```c
extern int objc_sync_enter(id obj);
```

## Return Value

OBJC_SYNC_SUCCESS once lock is acquired.

## Parameters

- `obj`: The object to begin synchronizing on.

## See Also

### Functions
- [class_createInstanceFromZone](./class_createinstancefromzone.md)
- [func class_lookupMethod(AnyClass?, Selector) -> IMP?](./class_lookupmethod%28_,_%29.md)
- [func class_respondsToMethod(AnyClass?, Selector) -> Bool](./class_respondstomethod%28_,_%29.md)
- [NXCompareHashTables](./nxcomparehashtables.md)
- [NXCopyHashTable](./nxcopyhashtable.md)
- [NXCountHashTable](./nxcounthashtable.md)
- [NXCreateHashTable](./nxcreatehashtable.md)
- [NXCreateHashTableFromZone](./nxcreatehashtablefromzone.md)
- [NXEmptyHashTable](./nxemptyhashtable.md)
- [NXFreeHashTable](./nxfreehashtable.md)
- [NXHashGet](./nxhashget.md)
- [NXHashInsert](./nxhashinsert.md)
- [NXHashInsertIfAbsent](./nxhashinsertifabsent.md)
- [NXHashMember](./nxhashmember.md)
- [NXHashRemove](./nxhashremove.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/objc_sync_enter)*