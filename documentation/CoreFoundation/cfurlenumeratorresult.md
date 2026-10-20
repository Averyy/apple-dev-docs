# CFURLEnumeratorResult

**Framework**: Core Foundation  
**Kind**: enum  
**Role**: Enumeration

Result codes from the [`CFURLEnumeratorGetNextURL(_:_:_:)`](./cfurlenumeratorgetnexturl%28_,_,_%29.md) function.

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
enum CFURLEnumeratorResult
```

```c
enum CFURLEnumeratorResult : CFIndex;
```

## Topics

### Constants
- [CFURLEnumeratorResult.success](./cfurlenumeratorresult/success.md)
  The enumerator was advanced successfully and returned a valid URL.
- [CFURLEnumeratorResult.end](./cfurlenumeratorresult/end.md)
  The enumeration is complete.
- [CFURLEnumeratorResult.error](./cfurlenumeratorresult/error.md)
  An error occurred during enumeration. The `error` parameter of the function is populated with error information.
- [CFURLEnumeratorResult.directoryPostOrderSuccess](./cfurlenumeratorresult/directorypostordersuccess.md)
  The recursive post-order enumerator returned the URL for a directory after having returned the URLs for all of the directory’s descendents.
### Initializers
- [init?(rawValue: CFIndex)](./cfurlenumeratorresult/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Enumerations
- [struct CFFileSecurityClearOptions](./cffilesecurityclearoptions.md)
- [struct CFISO8601DateFormatOptions](./cfiso8601dateformatoptions.md)
- [enum CFRunLoopRunResult](./cfrunlooprunresult.md)
- [struct CFURLEnumeratorOptions](./cfurlenumeratoroptions.md)
  Options for controlling enumerator behavior.
- [enum CGRectEdge](./cgrectedge.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlenumeratorresult)*