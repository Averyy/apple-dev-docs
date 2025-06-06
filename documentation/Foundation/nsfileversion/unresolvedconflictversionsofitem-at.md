# unresolvedConflictVersionsOfItem(at:)

**Framework**: Foundation  
**Kind**: method

Returns an array of version objects that are currently in conflict for the specified URL.

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
class func unresolvedConflictVersionsOfItem(at url: URL) -> [NSFileVersion]?
```

#### Return Value

An array of `NSFileVersion` objects that represent the versions in conflict or `nil` if the file at URL does not exist.

## Parameters

- `url`: The URL of the file that has associated version objects.

## See Also

- [var isConflict: Bool](nsfileversion/isconflict.md)
  A Boolean value indicating whether the contents of the version are in conflict with the contents of another version.
- [var isResolved: Bool](nsfileversion/isresolved.md)
  A Boolean value that indicates the version object is not in conflict ([`true`](https://developer.apple.com/documentation/swift/true)) or is in conflict ([`false`](https://developer.apple.com/documentation/swift/false)).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfileversion/unresolvedconflictversionsofitem(at:))*