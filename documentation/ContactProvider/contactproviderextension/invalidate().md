# invalidate()

**Framework**: ContactProvider  
**Kind**: method  
**Required**: Yes

Invalidates the extension.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
func invalidate() async throws
```

#### Discussion

The system calls this method before terminating the extension. The extension may complete termination before this method returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactproviderextension/invalidate())*