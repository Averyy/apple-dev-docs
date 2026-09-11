# assign(count:to:)

**Framework**: Foundation  
**Kind**: method

Adds a `ProgressReporter` as a child, with its progress representing a portion of `self`’s progress.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
final func assign(count: Int, to reporter: ProgressReporter)
```

#### Discussion

If a cycle is detected, this will cause a crash at runtime.

## Parameters

- `count`: Units, which is a portion of `totalCount`delegated to an instance of `Subprogress`.
- `reporter`: A `ProgressReporter` instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progressmanager/assign(count:to:)-98a77)*