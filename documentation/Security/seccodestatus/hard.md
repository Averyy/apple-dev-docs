# hard

**Framework**: Security  
**Kind**: property

The code prefers to be denied access to resources if gaining access would invalidate it.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
static var hard: SecCodeStatus { get }
```

#### Discussion

This bit can not be cleared on running code; it can only be set. It is undefined whether code that has the hard flag set but that starts out with the valid bit cleared (that is, it’s already invalid) will still be denied access to a resource that would invalidate it if it were still valid. That is, the code may or may not get access to such a resource while being invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccodestatus/hard)*