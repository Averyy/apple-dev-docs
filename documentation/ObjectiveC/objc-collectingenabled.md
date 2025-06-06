# objc_collectingEnabled()

**Framework**: Objective-C Runtime  
**Kind**: func

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+
- Unknown ?+ - Deprecated
- macOS ?+

## Declaration

```swift
func objc_collectingEnabled() -> Bool
```

## See Also

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
- [func objc_end_catch()](objc_end_catch().md)
- [func objc_enumerateClasses(fromImage: ObjCEnumerationImage, matchingNamePrefix: String?, conformingTo: Protocol?, subclassing: AnyClass?) -> ObjCClassList](objc_enumerateclasses(fromimage:matchingnameprefix:conformingto:subclassing:).md)
- [func objc_exception_rethrow() -> Never](objc_exception_rethrow().md)
- [func objc_exception_throw(Any) -> Never](objc_exception_throw(_:).md)
  Throw a runtime exception. This function is inserted by the compiler where \c @throw would otherwise be.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/objc_collectingenabled())*