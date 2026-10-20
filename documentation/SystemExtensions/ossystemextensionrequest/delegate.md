# delegate

**Framework**: System Extensions  
**Kind**: property  
**Role**: Instance Property

A delegate to receive updates about the progress of a request.

**Availability**:
- macOS 10.15+

## Declaration

```swift
weak var delegate: (any OSSystemExtensionRequestDelegate)? { get set }
```

```objc
@property (nonatomic, weak) id<OSSystemExtensionRequestDelegate> delegate;
```

## See Also

### Working with a Delegate
- [protocol OSSystemExtensionRequestDelegate](../ossystemextensionrequestdelegate.md)
  A type that receives updates about the progress of a request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemextensions/ossystemextensionrequest/delegate)*