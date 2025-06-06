# equal

**Framework**: Core Foundation  
**Kind**: property

An equality test callback for your program-defined `info` pointer. Can be `NULL`.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var equal: ((UnsafeRawPointer?, UnsafeRawPointer?) -> DarwinBoolean)!
```

#### Return Value

`true` if `info1` and `info2` should be considered equal; otherwise `false`.

#### Discussion

An equality test callback for your program-defined `info` pointer. Can be `NULL`.

## Parameters

- `info1`: The   member of the   or   structure that was used when creating the first run loop source to test.
- `info2`: The   member of the   or   structure that was used when creating the second run loop source to test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext1/equal)*