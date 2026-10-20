# Objective-C Functions

**Framework**: Objective-C Runtime  
**Role**: API Collection

## Topics

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
- [func objc_exception_throw(Any) -> Never](./objc_exception_throw%28_%29.md)
  Throw a runtime exception. This function is inserted by the compiler where \c @throw would otherwise be.
- [func objc_finalizeOnMainThread(AnyClass!)](./objc_finalizeonmainthread%28_%29.md)
- [func objc_is_finalized(UnsafeMutableRawPointer!) -> Bool](./objc_is_finalized%28_%29.md)
- [func objc_memmove_collectable(UnsafeMutableRawPointer!, UnsafeRawPointer!, Int) -> UnsafeMutableRawPointer!](./objc_memmove_collectable%28_,_,_%29.md)
- [func objc_registerThreadWithCollector()](./objc_registerthreadwithcollector%28%29.md)
- [func objc_removeExceptionHandler(UInt)](./objc_removeexceptionhandler%28_%29.md)
- [func objc_set_collection_ratio(Int)](./objc_set_collection_ratio%28_%29.md)
- [func objc_set_collection_threshold(Int)](./objc_set_collection_threshold%28_%29.md)
- [func objc_setCollectionRatio(Int)](./objc_setcollectionratio%28_%29.md)
- [func objc_setCollectionThreshold(Int)](./objc_setcollectionthreshold%28_%29.md)
- [func objc_setExceptionMatcher(objc_exception_matcher) -> objc_exception_matcher](./objc_setexceptionmatcher%28_%29.md)
- [func objc_setExceptionPreprocessor(objc_exception_preprocessor) -> objc_exception_preprocessor](./objc_setexceptionpreprocessor%28_%29.md)
- [func objc_setForwardHandler(UnsafeMutableRawPointer, UnsafeMutableRawPointer)](./objc_setforwardhandler%28_,_%29.md)
  Set the function to be called by objc_msgForward.
- [func objc_setHook_getClass(objc_hook_getClass, UnsafeMutablePointer<objc_hook_getClass?>)](./objc_sethook_getclass%28_,_%29.md)
- [func objc_setHook_getImageName(objc_hook_getImageName, UnsafeMutablePointer<objc_hook_getImageName?>)](./objc_sethook_getimagename%28_,_%29.md)
- [func objc_setHook_lazyClassNamer(objc_hook_lazyClassNamer, UnsafeMutablePointer<objc_hook_lazyClassNamer>)](./objc_sethook_lazyclassnamer%28_,_%29.md)
- [func objc_setUncaughtExceptionHandler(objc_uncaught_exception_handler) -> objc_uncaught_exception_handler](./objc_setuncaughtexceptionhandler%28_%29.md)
- [func objc_start_collector_thread()](./objc_start_collector_thread%28%29.md)
- [func objc_startCollectorThread()](./objc_startcollectorthread%28%29.md)
- [func objc_terminate() -> Never](./objc_terminate%28%29.md)
- [func objc_unregisterThreadWithCollector()](./objc_unregisterthreadwithcollector%28%29.md)
- [func object_isClass(Any?) -> Bool](./object_isclass%28_%29.md)
- [func object_setIvarWithStrongDefault(Any?, Ivar, Any?)](./object_setivarwithstrongdefault%28_,_,_%29.md)
- [func protocol_copyPropertyList2(Protocol, UnsafeMutablePointer<UInt32>?, Bool, Bool) -> UnsafeMutablePointer<objc_property_t>?](./protocol_copypropertylist2%28_,_,_,_%29.md)
- [func sel_isMapped(Selector) -> Bool](./sel_ismapped%28_%29.md)
  Identifies a selector as being valid or invalid.

## See Also

### Reference
- [Objective-C Runtime](./objective-c-runtime.md)
  Describes the macOS Objective-C runtime library support functions and data structures.
- [Objective-C Structures](./objective-c-structures.md)
- [Objective-C Constants](./objective-c-constants.md)
- [Objective-C Data Types](./objective-c-data-types.md)
- [Objective-C Macros](./objective-c-macros.md)
- [Objective-C Enumerations](./objective-c-enums.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/objective-c-functions)*