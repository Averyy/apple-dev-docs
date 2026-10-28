# retainCount

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Do not use this method.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```objc
- (NSUInteger) retainCount;
```

## Return Value

The receiver’s reference count.

## Discussion

This method is of no value in debugging memory management issues. Because any number of framework objects may have retained an object in order to hold references to it, while at the same time autorelease pools may be holding any number of deferred releases on an object, it is very unlikely that you can get useful information from this method.

To understand the fundamental rules of memory management that you must abide by, read [Memory Management Policy](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/MemoryMgmt/Articles/mmRules.html#//apple_ref/doc/uid/20000994). To diagnose memory management problems, use a suitable tool:

- The [Clang Static analyzer](http://clang-analyzer.llvm.org) can typically find memory management problems even before you run your program.
- The Object Alloc instrument in the Instruments application (see [Instruments User Guide](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/InstrumentsUserGuide/index.html#//apple_ref/doc/uid/TP40004652)) can track object allocation and destruction.

## See Also

### Obsolete Methods
- [- retain](./retain.md)
  Increments the receiver’s reference count.
- [- release](./release.md)
  Decrements the receiver’s reference count.
- [- autorelease](./autorelease.md)
  Decrements the receiver’s retain count at the end of the current autorelease pool block.
- [- zone](./zone.md)
  Zones are deprecated and ignored by most classes that have it as a parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-c.protocol/retaincount)*