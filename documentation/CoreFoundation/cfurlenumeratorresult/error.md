# CFURLEnumeratorResult.error

**Framework**: Core Foundation  
**Kind**: case  
**Role**: Case

An error occurred during enumeration. The `error` parameter of the function is populated with error information.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
case error
```

```c
kCFURLEnumeratorError
```

## See Also

### Constants
- [CFURLEnumeratorResult.success](./success.md)
  The enumerator was advanced successfully and returned a valid URL.
- [CFURLEnumeratorResult.end](./end.md)
  The enumeration is complete.
- [CFURLEnumeratorResult.directoryPostOrderSuccess](./directorypostordersuccess.md)
  The recursive post-order enumerator returned the URL for a directory after having returned the URLs for all of the directory’s descendents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlenumeratorresult/error)*