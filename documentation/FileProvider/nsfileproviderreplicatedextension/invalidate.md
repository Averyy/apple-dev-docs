# invalidate()

**Framework**: Fileprovider  
**Kind**: method  
**Required**: Yes

Tells the file provider to perform any necessary cleanup so that the system can deallocate it.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func invalidate()
```

#### Discussion

Your implementation should perform any necessary cleanup so that the system can dismiss and deallocate the file provider.

> **Note**:  Your extension must handle multiple active copies of the File Provider extension in the same process, for instance, if the user has several active domains, or when the system discards one instance while initiating another.

## See Also

- [init(domain: NSFileProviderDomain)](nsfileproviderreplicatedextension/init(domain:).md)
  Creates an instance of the file provider for the specified domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderreplicatedextension/invalidate())*