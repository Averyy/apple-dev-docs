# getDescent

**Framework**: Core Text  
**Kind**: property  
**Role**: Instance Property

The callback invoked to request the run delegate to determine and return the typographic descent of glyphs in the run. This callback may be `NULL`, which is equivalent to a `getDescent` callback that always returns 0.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var getDescent: CTRunDelegateGetDescentCallback
```

```c
CTRunDelegateGetDescentCallback getDescent;
```

## See Also

### Instance Properties
- [var dealloc: CTRunDelegateDeallocateCallback](./dealloc.md)
  The callback invoked when the retain count of a CTRunDelegate reaches 0 and the CTRunDelegate is deallocated. This callback may be `NULL`.
- [var getAscent: CTRunDelegateGetAscentCallback](./getascent.md)
  The callback invoked to request the run delegate to determine and return the typographic ascent of glyphs in the run. This callback may be `NULL`, which is equivalent to a `getAscent` callback that always returns 0.
- [var getWidth: CTRunDelegateGetWidthCallback](./getwidth.md)
  The callback invoked to request the run delegate to determine and return the typographic width of glyphs in the run. This callback may be `NULL`, which is equivalent to a `getWidth` callback that always returns 0.
- [var version: CFIndex](./version.md)
  The version number of the callbacks being passed in as a parameter to [`CTRunDelegateCreate(_:_:)`](../ctrundelegatecreate%28_,_%29.md). The initial version is [`kCTRunDelegateVersion1`](../kctrundelegateversion1.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctrundelegatecallbacks/getdescent)*