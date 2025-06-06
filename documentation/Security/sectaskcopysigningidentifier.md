# SecTaskCopySigningIdentifier(_:_:)

**Framework**: Security  
**Kind**: func

Returns the value of the code signing identifier.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func SecTaskCopySigningIdentifier(_ task: SecTask, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFString?
```

#### Return Value

A string representing the code signing identifier for the task, or `NULL` on error. In Objective-C, call the [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) function to free this string’s memory when you are done with it.

## Parameters

- `task`: The task whose code signing identifier you want.
- `error`: A pointer that the function uses to provide an error object with details if an error occurs. The caller becomes responsible for the object’s memory. Pass   to ignore the error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectaskcopysigningidentifier(_:_:))*