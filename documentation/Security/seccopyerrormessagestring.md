# SecCopyErrorMessageString(_:_:)

**Framework**: Security  
**Kind**: func

Returns a string explaining the meaning of a security result code.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS 11.3+
- visionOS 1.0+
- watchOS 4.3+

## Declaration

```swift
func SecCopyErrorMessageString(_ status: OSStatus, _ reserved: UnsafeMutableRawPointer?) -> CFString?
```

#### Return Value

A human-readable string describing the result, or `nil` if no string is available for the specified result code. In Objective-C, call the [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) function to release this object when you are finished using it.

## Parameters

- `status`: A result code of type   returned by a security function. See   for a list of codes.
- `reserved`: Reserved for future use. Pass   for this parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccopyerrormessagestring(_:_:))*