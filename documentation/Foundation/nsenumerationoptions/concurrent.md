# concurrent

**Framework**: Foundation  
**Kind**: property

Specifies that the Block enumeration should be concurrent.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var concurrent: NSEnumerationOptions { get }
```

#### Discussion

The order of invocation is nondeterministic and undefined; this flag is a hint and may be ignored by the implementation under some circumstances; the code of the Block must be safe against concurrent invocation.

## See Also

- [static var reverse: NSEnumerationOptions](nsenumerationoptions/reverse.md)
  Specifies that the enumeration should be performed in reverse.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsenumerationoptions/concurrent)*