# init(rebasing:)

**Framework**: Swift  
**Kind**: init

Creates a buffer over the same memory as the given buffer slice.

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
init(rebasing slice: Slice<UnsafeBufferPointer<Element>>)
```

#### Discussion

The new buffer represents the same region of memory as `slice`, but is indexed starting at zero instead of sharing indices with the original buffer. For example:

```swift
let buffer = returnsABuffer()
let n = 5
let slice = buffer[n...]
let rebased = UnsafeBufferPointer(rebasing: slice)
```

After rebasing `slice` as the `rebased` buffer, the following are true:

- `rebased.startIndex == 0`
- `rebased[0] == slice[n]`
- `rebased[0] == buffer[n]`
- `rebased.count == slice.count`

## Parameters

- `slice`: The buffer slice to rebase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafebufferpointer/init(rebasing:)-56rdb)*