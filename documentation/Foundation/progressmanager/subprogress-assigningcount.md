# subprogress(assigningCount:)

**Framework**: Foundation  
**Kind**: method

Returns a `Subprogress` representing a portion of `self` which can be passed to any method that reports progress.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
final func subprogress(assigningCount portionOfParentTotal: Int) -> Subprogress
```

#### Return Value

A `Subprogress` instance.

#### Discussion

If the `Subprogress` is not converted into a `ProgressManager` (for example, due to an error or early return), then the assigned count is marked as completed in the parent `ProgressManager`.

## Parameters

- `portionOfParentTotal`: The portion of `totalCount` to be delegated to the `Subprogress`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progressmanager/subprogress(assigningcount:))*