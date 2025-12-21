# init(buffer:initializedCount:)

**Framework**: Swift  
**Kind**: init

Unsafely create an OutputRawSpan over partly-initialized memory.

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 12.2+
- macOS 10.14.4+
- tvOS 12.2+
- visionOS 1.0+
- watchOS 5.2+

## Declaration

```swift
init(buffer: borrowing Slice<UnsafeMutableRawBufferPointer>, initializedCount: Int)
```

#### Discussion

The memory in `buffer` must remain valid throughout the lifetime of the newly-created `OutputRawSpan`. Its prefix must contain `initializedCount` initialized bytes, followed by uninitialized memory.

## Parameters

- `buffer`: An   to be initialized
- `initializedCount`: The number of initialized bytes   at the beginning of  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/outputrawspan/init(buffer:initializedcount:)-5sduz)*