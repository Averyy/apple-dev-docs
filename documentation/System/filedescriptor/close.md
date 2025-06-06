# close()

**Framework**: System  
**Kind**: method

Deletes a file descriptor.

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
func close() throws
```

## Mentions

- [Adopting Swift File Operations](adopting-file-operations.md)

#### Discussion

Deletes the file descriptor from the per-process object reference table. If this is the last reference to the underlying object, the object will be deactivated.

The corresponding C function is `close`.

## See Also

- [func closeAfter<R>(() throws -> R) throws -> R](filedescriptor/closeafter(_:).md)
  Runs a closure and then closes the file descriptor, even if an error occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filedescriptor/close())*