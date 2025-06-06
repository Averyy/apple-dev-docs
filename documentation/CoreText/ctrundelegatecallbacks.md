# CTRunDelegateCallbacks

**Framework**: Core Text  
**Kind**: struct

A structure holding pointers to callbacks implemented by the run delegate.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct CTRunDelegateCallbacks
```

#### Overview

You pass in a pointer to this structure when you create a CTRunDelegate object with the [`CTRunDelegateCreate(_:_:)`](ctrundelegatecreate(_:_:).md) function. The callbacks defined in this structure are provided by the owner of a run delegate and are used to modify glyph metrics during layout. The values returned by the delegate are applied to each glyph in the run or runs corresponding to the attribute containing that delegate.

See [`CTRunDelegate`](ctrundelegate.md) for a discussion of the function-pointer types associated with these callbacks.

## Topics

### Initializers
- [init(version: CFIndex, dealloc: CTRunDelegateDeallocateCallback, getAscent: CTRunDelegateGetAscentCallback, getDescent: CTRunDelegateGetDescentCallback, getWidth: CTRunDelegateGetWidthCallback)](ctrundelegatecallbacks/init(version:dealloc:getascent:getdescent:getwidth:).md)
### Instance Properties
- [var dealloc: CTRunDelegateDeallocateCallback](ctrundelegatecallbacks/dealloc.md)
  The callback invoked when the retain count of a CTRunDelegate reaches 0 and the CTRunDelegate is deallocated. This callback may be `NULL`.
- [var getAscent: CTRunDelegateGetAscentCallback](ctrundelegatecallbacks/getascent.md)
  The callback invoked to request the run delegate to determine and return the typographic ascent of glyphs in the run. This callback may be `NULL`, which is equivalent to a `getAscent` callback that always returns 0.
- [var getDescent: CTRunDelegateGetDescentCallback](ctrundelegatecallbacks/getdescent.md)
  The callback invoked to request the run delegate to determine and return the typographic descent of glyphs in the run. This callback may be `NULL`, which is equivalent to a `getDescent` callback that always returns 0.
- [var getWidth: CTRunDelegateGetWidthCallback](ctrundelegatecallbacks/getwidth.md)
  The callback invoked to request the run delegate to determine and return the typographic width of glyphs in the run. This callback may be `NULL`, which is equivalent to a `getWidth` callback that always returns 0.
- [var version: CFIndex](ctrundelegatecallbacks/version.md)
  The version number of the callbacks being passed in as a parameter to [`CTRunDelegateCreate(_:_:)`](ctrundelegatecreate(_:_:).md). The initial version is [`kCTRunDelegateVersion1`](kctrundelegateversion1.md).

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctrundelegatecallbacks)*