# objc_set_collection_threshold(_:)

**Framework**: Objective-C Runtime  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

> **Deprecated**: it does nothing. Define OBJC_SILENCE_GC_DEPRECATIONS=1 to temporarily silence this diagnostic.

## Declaration

```swift
func objc_set_collection_threshold(_ threshold: Int)
```

```c
static void objc_set_collection_threshold(size_t threshold);
```

## See Also

### Functions
- [func autoreleasepool<E, Result>(invoking: () throws(E) -> Result) throws(E) -> Result](./autoreleasepool%28invoking%29.md)
- [func class_lookupMethod(AnyClass?, Selector) -> IMP?](./class_lookupmethod%28_,_%29.md)
- [func class_respondsToMethod(AnyClass?, Selector) -> Bool](./class_respondstomethod%28_,_%29.md)
- [func objc_addExceptionHandler(objc_exception_handler, UnsafeMutableRawPointer?) -> UInt](./objc_addexceptionhandler%28_,_%29.md)
- [func objc_addLoadImageFunc(objc_func_loadImage)](./objc_addloadimagefunc%28_%29.md)
- [func objc_assertRegisteredThreadWithCollector()](./objc_assertregisteredthreadwithcollector%28%29.md)
- [func objc_begin_catch(UnsafeMutableRawPointer) -> Any](./objc_begin_catch%28_%29.md)
- [func objc_clear_stack(UInt)](./objc_clear_stack%28_%29.md)
- [func objc_collect(UInt)](./objc_collect%28_%29.md)
- [func objc_collectableZone() -> objc_zone_t!](./objc_collectablezone%28%29.md)
- [func objc_collecting_enabled() -> Bool](./objc_collecting_enabled%28%29.md)
- [func objc_collectingEnabled() -> Bool](./objc_collectingenabled%28%29.md)
- [func objc_end_catch()](./objc_end_catch%28%29.md)
- [func objc_enumerateClasses(fromImage: ObjCEnumerationImage, matchingNamePrefix: String?, conformingTo: Protocol?, subclassing: AnyClass?) -> ObjCClassList](./objc_enumerateclasses%28fromimage,matchingnameprefix,conformingto,subclassing%29.md)
- [func objc_exception_rethrow() -> Never](./objc_exception_rethrow%28%29.md)
- [class_createInstanceFromZone](./class_createinstancefromzone.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/objc_set_collection_threshold(_:))*