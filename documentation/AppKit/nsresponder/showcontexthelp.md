# showContextHelp(_:)

**Framework**: AppKit  
**Kind**: method

Implemented by subclasses to invoke the help system, displaying information relevant to the receiver and its current state.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func showContextHelp(_ sender: Any?)
```

## Parameters

- `sender`: Typically the object that invoked this method.

## See Also

- [func helpRequested(NSEvent)](nsresponder/helprequested(_:).md)
  Displays context-sensitive help for the receiver if help has been registered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/showcontexthelp(_:))*