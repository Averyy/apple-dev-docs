# CTRunDelegateCreate(_:_:)

**Framework**: Core Text  
**Kind**: func

Creates an immutable instance of a run delegate.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CTRunDelegateCreate(_ callbacks: UnsafePointer<CTRunDelegateCallbacks>, _ refCon: UnsafeMutableRawPointer?) -> CTRunDelegate?
```

#### Return Value

If  successful, a reference to an immutable CTRunDelegate object. Otherwise, returns `NULL`.

#### Discussion

The run-delegate object can be used for reserving space in a line or for eliding the glyphs for a range of text altogether.

## Parameters

- `callbacks`: A structure holding pointers to the callbacks for this run delegate.
- `refCon`: A constant value associated with the run delegate to identify it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctrundelegatecreate(_:_:))*