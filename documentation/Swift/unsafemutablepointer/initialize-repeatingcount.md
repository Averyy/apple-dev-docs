# initialize(repeating:count:)

**Framework**: Swift  
**Kind**: method

Initializes this pointer’s memory with the specified number of consecutive copies of the given value.

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
func initialize(repeating repeatedValue: Pointee, count: Int)
```

#### Discussion

The destination memory must be uninitialized or the pointer’s `Pointee` must be a trivial type. After a call to `initialize(repeating:count:)`, the memory referenced by this pointer is initialized.

## Parameters

- `repeatedValue`: The instance to initialize this pointer’s memory with.
- `count`: The number of consecutive copies of   to initialize.    must not be negative.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablepointer/initialize(repeating:count:))*