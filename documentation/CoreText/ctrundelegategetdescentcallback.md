# CTRunDelegateGetDescentCallback

**Framework**: Core Text  
**Kind**: typealias  
**Role**: Type Alias

Defines a pointer to a function that determines typographic descent of glyphs in the run.

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
typealias CTRunDelegateGetDescentCallback = (UnsafeMutableRawPointer) -> CGFloat
```

```c
typedef double (*)(void *) CTRunDelegateGetDescentCallback;
```

## Return Value

The typographic descent of glyphs in the run associated with the run delegate.

## Discussion

You would declare the get-descent function like this if you were to name it `MyGetDescentCallback`:

## Parameters

- `refCon`: The reference-constant value supplied to the [`CTRunDelegateCreate(_:_:)`](./ctrundelegatecreate%28_,_%29.md) function when the run delegate was created.

## See Also

### Callbacks
- [typealias CTRunDelegateGetAscentCallback](./ctrundelegategetascentcallback.md)
  Defines a pointer to a function that determines typographic ascent of glyphs in the run.
- [typealias CTRunDelegateGetWidthCallback](./ctrundelegategetwidthcallback.md)
  Defines a pointer to a function that determines the typographic width of glyphs in the run.
- [typealias CTRunDelegateDeallocateCallback](./ctrundelegatedeallocatecallback.md)
  Defines a pointer to a function that is invoked when a CTRunDelegate object is deallocated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctrundelegategetdescentcallback)*