# isConflict

**Framework**: Foundation  
**Kind**: property

A Boolean value indicating whether the contents of the version are in conflict with the contents of another version.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isConflict: Bool { get }
```

#### Discussion

When two or more versions of a file are written at the same time, perhaps because the file is saved in the cloud and one or more of the writers were offline when they were writing, the system attempts to resolve the conflict automatically. It does this by picking one of the file versions to be the current file and setting this property to [`true`](https://developer.apple.com/documentation/swift/true) for the other file versions that are in conflict.

## See Also

- [var isResolved: Bool](nsfileversion/isresolved.md)
  A Boolean value that indicates the version object is not in conflict ([`true`](https://developer.apple.com/documentation/swift/true)) or is in conflict ([`false`](https://developer.apple.com/documentation/swift/false)).
- [class func unresolvedConflictVersionsOfItem(at: URL) -> [NSFileVersion]?](nsfileversion/unresolvedconflictversionsofitem(at:).md)
  Returns an array of version objects that are currently in conflict for the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfileversion/isconflict)*