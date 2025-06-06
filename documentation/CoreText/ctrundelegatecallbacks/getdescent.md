# getDescent

**Framework**: Core Text  
**Kind**: property

The callback invoked to request the run delegate to determine and return the typographic descent of glyphs in the run. This callback may be `NULL`, which is equivalent to a `getDescent` callback that always returns 0.

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
var getDescent: CTRunDelegateGetDescentCallback
```

## See Also

- [var dealloc: CTRunDelegateDeallocateCallback](ctrundelegatecallbacks/dealloc.md)
  The callback invoked when the retain count of a CTRunDelegate reaches 0 and the CTRunDelegate is deallocated. This callback may be `NULL`.
- [var getAscent: CTRunDelegateGetAscentCallback](ctrundelegatecallbacks/getascent.md)
  The callback invoked to request the run delegate to determine and return the typographic ascent of glyphs in the run. This callback may be `NULL`, which is equivalent to a `getAscent` callback that always returns 0.
- [var getWidth: CTRunDelegateGetWidthCallback](ctrundelegatecallbacks/getwidth.md)
  The callback invoked to request the run delegate to determine and return the typographic width of glyphs in the run. This callback may be `NULL`, which is equivalent to a `getWidth` callback that always returns 0.
- [var version: CFIndex](ctrundelegatecallbacks/version.md)
  The version number of the callbacks being passed in as a parameter to [`CTRunDelegateCreate(_:_:)`](ctrundelegatecreate(_:_:).md). The initial version is [`kCTRunDelegateVersion1`](kctrundelegateversion1.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctrundelegatecallbacks/getdescent)*