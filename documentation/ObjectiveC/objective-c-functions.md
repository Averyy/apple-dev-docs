# Objective-C Functions

**Framework**: Objective-C Runtime

## Topics

### Functions
- [func autoreleasepool<E, Result>(invoking: () throws(E) -> Result) throws(E) -> Result](autoreleasepool(invoking:).md)
- [func class_lookupMethod(AnyClass?, Selector) -> IMP?](class_lookupmethod(_:_:).md)
- [func class_respondsToMethod(AnyClass?, Selector) -> Bool](class_respondstomethod(_:_:).md)
- [func objc_addExceptionHandler(objc_exception_handler, UnsafeMutableRawPointer?) -> UInt](objc_addexceptionhandler(_:_:).md)
- [func objc_addLoadImageFunc(objc_func_loadImage)](objc_addloadimagefunc(_:).md)
- [func objc_assertRegisteredThreadWithCollector()](objc_assertregisteredthreadwithcollector().md)
- [func objc_begin_catch(UnsafeMutableRawPointer) -> Any](objc_begin_catch(_:).md)
- [func objc_clear_stack(UInt)](objc_clear_stack(_:).md)
- [func objc_collect(UInt)](objc_collect(_:).md)
- [func objc_collectableZone() -> objc_zone_t!](objc_collectablezone().md)
- [func objc_collecting_enabled() -> Bool](objc_collecting_enabled().md)
- [func objc_collectingEnabled() -> Bool](objc_collectingenabled().md)
- [func objc_end_catch()](objc_end_catch().md)
- [func objc_enumerateClasses(fromImage: ObjCEnumerationImage, matchingNamePrefix: String?, conformingTo: Protocol?, subclassing: AnyClass?) -> ObjCClassList](objc_enumerateclasses(fromimage:matchingnameprefix:conformingto:subclassing:).md)
- [func objc_exception_rethrow() -> Never](objc_exception_rethrow().md)
- [func objc_exception_throw(Any) -> Never](objc_exception_throw(_:).md)
  Throw a runtime exception. This function is inserted by the compiler where \c @throw would otherwise be.
- [func objc_finalizeOnMainThread(AnyClass!)](objc_finalizeonmainthread(_:).md)
- [func objc_is_finalized(UnsafeMutableRawPointer!) -> Bool](objc_is_finalized(_:).md)
- [func objc_memmove_collectable(UnsafeMutableRawPointer!, UnsafeRawPointer!, Int) -> UnsafeMutableRawPointer!](objc_memmove_collectable(_:_:_:).md)
- [func objc_registerThreadWithCollector()](objc_registerthreadwithcollector().md)
- [func objc_removeExceptionHandler(UInt)](objc_removeexceptionhandler(_:).md)
- [func objc_set_collection_ratio(Int)](objc_set_collection_ratio(_:).md)
- [func objc_set_collection_threshold(Int)](objc_set_collection_threshold(_:).md)
- [func objc_setCollectionRatio(Int)](objc_setcollectionratio(_:).md)
- [func objc_setCollectionThreshold(Int)](objc_setcollectionthreshold(_:).md)
- [func objc_setExceptionMatcher(objc_exception_matcher) -> objc_exception_matcher](objc_setexceptionmatcher(_:).md)
- [func objc_setExceptionPreprocessor(objc_exception_preprocessor) -> objc_exception_preprocessor](objc_setexceptionpreprocessor(_:).md)
- [func objc_setForwardHandler(UnsafeMutableRawPointer, UnsafeMutableRawPointer)](objc_setforwardhandler(_:_:).md)
  Set the function to be called by objc_msgForward.
- [func objc_setHook_getClass(objc_hook_getClass, UnsafeMutablePointer<objc_hook_getClass?>)](objc_sethook_getclass(_:_:).md)
- [func objc_setHook_getImageName(objc_hook_getImageName, UnsafeMutablePointer<objc_hook_getImageName?>)](objc_sethook_getimagename(_:_:).md)
- [func objc_setHook_lazyClassNamer(objc_hook_lazyClassNamer, UnsafeMutablePointer<objc_hook_lazyClassNamer>)](objc_sethook_lazyclassnamer(_:_:).md)
- [func objc_setUncaughtExceptionHandler(objc_uncaught_exception_handler) -> objc_uncaught_exception_handler](objc_setuncaughtexceptionhandler(_:).md)
- [func objc_start_collector_thread()](objc_start_collector_thread().md)
- [func objc_startCollectorThread()](objc_startcollectorthread().md)
- [func objc_sync_enter(Any) -> Int32](objc_sync_enter(_:).md)
  Begin synchronizing on ‘obj’.
Allocates recursive pthread_mutex associated with ‘obj’ if needed.
- [func objc_sync_exit(Any) -> Int32](objc_sync_exit(_:).md)
  End synchronizing on ‘obj’.
- [func objc_terminate() -> Never](objc_terminate().md)
- [func objc_unregisterThreadWithCollector()](objc_unregisterthreadwithcollector().md)
- [func object_isClass(Any?) -> Bool](object_isclass(_:).md)
- [func object_setIvarWithStrongDefault(Any?, Ivar, Any?)](object_setivarwithstrongdefault(_:_:_:).md)
- [func protocol_copyPropertyList2(Protocol, UnsafeMutablePointer<UInt32>?, Bool, Bool) -> UnsafeMutablePointer<objc_property_t>?](protocol_copypropertylist2(_:_:_:_:).md)
- [func sel_isMapped(Selector) -> Bool](sel_ismapped(_:).md)
  Identifies a selector as being valid or invalid.

## See Also

- [Objective-C Runtime](objective-c-runtime.md)
  Describes the macOS Objective-C runtime library support functions and data structures.
- [Objective-C Structures](objective-c-structures.md)
- [Objective-C Constants](objective-c-constants.md)
- [Objective-C Data Types](objective-c-data-types.md)
- [Objective-C Macros](objective-c-macros.md)
- [Objective-C Enumerations](objective-c-enums.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/objective-c-functions)*