# object_setIvarWithStrongDefault(_:_:_:)

**Framework**: Objective-C Runtime  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func object_setIvarWithStrongDefault(_ obj: Any?, _ ivar: Ivar, _ value: Any?)
```

```c
extern void object_setIvarWithStrongDefault(id obj, Ivar ivar, id value);
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/object_setivarwithstrongdefault(_:_:_:))*