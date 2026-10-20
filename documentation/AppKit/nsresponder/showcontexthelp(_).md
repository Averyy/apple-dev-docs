# showContextHelp(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Implemented by subclasses to invoke the help system, displaying information relevant to the receiver and its current state.

**Availability**:
- macOS

## Declaration

```swift
func showContextHelp(_ sender: Any?)
```

```objc
- (void) showContextHelp:(id) sender;
```

## Parameters

- `sender`: Typically the object that invoked this method.

## See Also

### Related Documentation
- [func helpRequested(NSEvent)](./helprequested%28_%29.md)
  Displays context-sensitive help for the receiver if help has been registered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/showcontexthelp(_:))*