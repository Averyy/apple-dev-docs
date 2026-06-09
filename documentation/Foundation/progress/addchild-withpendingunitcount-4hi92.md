# addChild(_:withPendingUnitCount:)

**Framework**: Foundation  
**Kind**: method

Adds a ProgressReporter as a child to a Progress, which constitutes a portion of Progress’s totalUnitCount.

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
func addChild(_ reporter: ProgressReporter, withPendingUnitCount count: Int)
```

## Parameters

- `reporter`: A `ProgressReporter` instance.
- `count`: Number of units delegated from `self`’s `totalCount`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progress/addchild(_:withpendingunitcount:)-4hi92)*