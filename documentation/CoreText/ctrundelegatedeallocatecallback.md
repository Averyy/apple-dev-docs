# CTRunDelegateDeallocateCallback

**Framework**: Core Text  
**Kind**: typealias

Defines a pointer to a function that is invoked when a CTRunDelegate object is deallocated.

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
typealias CTRunDelegateDeallocateCallback = (UnsafeMutableRawPointer) -> Void
```

#### Discussion

You would declare the deallocation function like this if you were to name it `MyDeallocationCallback`:

## Parameters

- `refCon`: The reference-constant value supplied to the   function when the run delegate was created.

## See Also

- [typealias CTRunDelegateGetAscentCallback](ctrundelegategetascentcallback.md)
  Defines a pointer to a function that determines typographic ascent of glyphs in the run.
- [typealias CTRunDelegateGetDescentCallback](ctrundelegategetdescentcallback.md)
  Defines a pointer to a function that determines typographic descent of glyphs in the run.
- [typealias CTRunDelegateGetWidthCallback](ctrundelegategetwidthcallback.md)
  Defines a pointer to a function that determines the typographic width of glyphs in the run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctrundelegatedeallocatecallback)*