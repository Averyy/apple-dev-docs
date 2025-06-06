# closeAfter(_:)

**Framework**: System  
**Kind**: method

Runs a closure and then closes the file descriptor, even if an error occurs.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func closeAfter<R>(_ body: () throws -> R) throws -> R
```

#### Return Value

The value returned by the closure.

#### Discussion

If `body` throws an error or an error occurs while closing the file descriptor, this method rethrows that error.

## Parameters

- `body`: The closure to run.   If the closure throws an error,   this method closes the file descriptor before it rethrows that error.

## See Also

- [func close() throws](filedescriptor/close.md)
  Deletes a file descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filedescriptor/closeafter(_:))*