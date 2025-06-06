# CFLocaleCopyPreferredLanguages()

**Framework**: Core Foundation  
**Kind**: func

Returns the array of canonicalized language IDs that the user prefers.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CFLocaleCopyPreferredLanguages() -> CFArray!
```

#### Return Value

The array of canonicalized `CFString` language IDs that the current user prefers. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cflocalecopypreferredlanguages())*