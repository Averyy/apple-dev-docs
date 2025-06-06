# update(repeating:)

**Framework**: Swift  
**Kind**: method

Updates every element of this buffer slice’s initialized memory.

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
func update<Element>(repeating repeatedValue: Element) where Base == UnsafeMutableBufferPointer<Element>
```

#### Discussion

The buffer slice’s memory must be initialized or its `Element` must be a trivial type.

> **Note**: All buffer elements must already be initialized.

All buffer elements must already be initialized.

## Parameters

- `repeatedValue`: The value used when updating this pointer’s memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/slice/update(repeating:))*