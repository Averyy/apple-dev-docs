# init(buffer:initializedCount:)

**Framework**: Swift  
**Kind**: init

Unsafely create an OutputSpan over partly-initialized memory.

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
init(buffer: borrowing Slice<UnsafeMutableBufferPointer<Element>>, initializedCount: Int)
```

#### Discussion

The memory in `buffer` must remain valid throughout the lifetime of the newly-created `OutputSpan`. Its prefix must contain `initializedCount` initialized instances, followed by uninitialized memory. The default value of `initializedCount` is 0, representing the common case of a completely uninitialized `buffer`.

## Parameters

- `buffer`: An   to be initialized
- `initializedCount`: The number of initialized elements   at the beginning of  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/outputspan/init(buffer:initializedcount:)-vie3)*