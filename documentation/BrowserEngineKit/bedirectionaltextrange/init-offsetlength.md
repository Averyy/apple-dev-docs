# init(offset:length:)

**Framework**: BrowserEngineKit  
**Kind**: init

Creates a range for a text selection that also specifies a direction.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
init(offset: Int, length: Int)
```

#### Discussion

The sign of the `length` argument determines the selection’s direction from the `offset` argument.

## See Also

- [init()](bedirectionaltextrange/init.md)
  Creates an empty directional text range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bedirectionaltextrange/init(offset:length:))*