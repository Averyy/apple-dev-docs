# objc_setForwardHandler(_:_:)

**Framework**: Objective-C Runtime  
**Kind**: func

Set the function to be called by objc_msgForward.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func objc_setForwardHandler(_ fwd: UnsafeMutableRawPointer, _ fwd_stret: UnsafeMutableRawPointer)
```

## Parameters

- `fwd`: Function to be jumped to by objc_msgForward.
- `fwd_stret`: Function to be jumped to by objc_msgForward_stret.

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
- [func objc_collectingEnabled() -> Bool](objc_collectingenabled().md)
- [func objc_end_catch()](objc_end_catch().md)
- [func objc_enumerateClasses(fromImage: ObjCEnumerationImage, matchingNamePrefix: String?, conformingTo: Protocol?, subclassing: AnyClass?) -> ObjCClassList](objc_enumerateclasses(fromimage:matchingnameprefix:conformingto:subclassing:).md)
- [func objc_exception_rethrow() -> Never](objc_exception_rethrow().md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/objc_setforwardhandler(_:_:))*