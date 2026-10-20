# isConflict

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly, getter=isConflict) BOOL conflict;
```

#### Discussion

When two or more versions of a file are written at the same time, perhaps because the file is saved in the cloud and one or more of the writers were offline when they were writing, the system attempts to resolve the conflict automatically. It does this by picking one of the file versions to be the current file and setting this property to [`true`](../../Swift/true.md) for the other file versions that are in conflict.

## See Also

### Handling Version Conflicts
- [var isResolved: Bool](./isresolved.md)
  A Boolean value that indicates if the version object is in conflict or not.
- [class func unresolvedConflictVersionsOfItem(at: URL) -> [NSFileVersion]?](./unresolvedconflictversionsofitem%28at%29.md)
  Returns an array of version objects that are currently in conflict for the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfileversion/isconflict)*