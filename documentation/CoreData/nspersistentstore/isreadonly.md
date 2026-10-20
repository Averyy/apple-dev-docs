# isReadOnly

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the persistent store is read-only.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isReadOnly: Bool { get set }
```

```objc
@property (getter=isReadOnly) BOOL readOnly;
```

#### Discussion

[`true`](../../Swift/true.md) if the receiver is read-only, otherwise [`false`](../../Swift/false.md).

## See Also

### Managing Store Attributes
- [var identifier: String!](./identifier.md)
  The unique identifier for the persistent store.
- [var url: URL?](./url.md)
  The URL for the persistent store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstore/isreadonly)*