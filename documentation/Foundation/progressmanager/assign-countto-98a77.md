# assign(count:to:)

**Framework**: Foundation  
**Kind**: method

Adds a `ProgressReporter` as a child, with its progress representing a portion of `self`’s progress.

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
final func assign(count: Int, to reporter: ProgressReporter)
```

#### Discussion

If a cycle is detected, this will cause a crash at runtime.

## Parameters

- `count`: Units, which is a portion of `totalCount`delegated to an instance of `Subprogress`.
- `reporter`: A `ProgressReporter` instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progressmanager/assign(count:to:)-98a77)*