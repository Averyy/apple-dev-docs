# init(rebasing:)

**Framework**: Swift  
**Kind**: init

Creates a raw buffer over the same memory as the given raw buffer slice, with the indices rebased to zero.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(rebasing slice: Slice<UnsafeMutableRawBufferPointer>)
```

#### Discussion

The new buffer represents the same region of memory as the slice, but its indices start at zero instead of at the beginning of the slice in the original buffer. The following code creates `slice`, a slice covering part of an existing buffer instance, then rebases it into a new `rebased` buffer.

```swift
let slice = buffer[n...]
let rebased = UnsafeRawBufferPointer(rebasing: slice)
```

After this code has executed, the following are true:

- `rebased.startIndex == 0`
- `rebased[0] == slice[n]`
- `rebased[0] == buffer[n]`
- `rebased.count == slice.count`

## Parameters

- `slice`: The raw buffer slice to rebase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablerawbufferpointer/init(rebasing:))*