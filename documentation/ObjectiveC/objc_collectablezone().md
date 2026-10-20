# objc_collectableZone()

**Framework**: Objective-C Runtime  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS

> **Deprecated**: it always returns nil. Define OBJC_SILENCE_GC_DEPRECATIONS=1 to temporarily silence this diagnostic.

## Declaration

```swift
func objc_collectableZone() -> objc_zone_t!
```

```c
static objc_zone_tobjc_collectableZone();
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
- [func objc_collecting_enabled() -> Bool](./objc_collecting_enabled%28%29.md)
- [func objc_collectingEnabled() -> Bool](./objc_collectingenabled%28%29.md)
- [func objc_end_catch()](./objc_end_catch%28%29.md)
- [func objc_enumerateClasses(fromImage: ObjCEnumerationImage, matchingNamePrefix: String?, conformingTo: Protocol?, subclassing: AnyClass?) -> ObjCClassList](./objc_enumerateclasses%28fromimage,matchingnameprefix,conformingto,subclassing%29.md)
- [func objc_exception_rethrow() -> Never](./objc_exception_rethrow%28%29.md)
- [func objc_exception_throw(Any) -> Never](./objc_exception_throw%28_%29.md)
  Throw a runtime exception. This function is inserted by the compiler where \c @throw would otherwise be.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/objc_collectablezone())*